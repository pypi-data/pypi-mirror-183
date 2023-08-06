"""Define Model Registry Manager."""
from functools import partial
from operator import attrgetter

from ML_management import mlmanagement
from ML_management.registry.exceptions import (
    MetricNotLogged,
    ModelNotRegistered,
    NoMetricProvided,
    NoVersionsOnStage,
    UnsupportedCriteria,
    VersionNotFound,
)

from mlflow.entities.model_registry.model_version import ModelVersion
from mlflow.entities.model_registry.registered_model import RegisteredModel
from mlflow.exceptions import RestException
from mlflow.store.entities import PagedList

# noinspection PyUnresolvedReferences


# TODO maybe make it singleton?


class RegistryManager:
    """Registry Manager to choose necessary version of the model."""

    def __init__(self):
        self.client = mlmanagement.MlflowClient()

    def check_model_registered(self, name: str) -> RegisteredModel:
        """Check if model is registered in mlflow or not."""
        try:
            registered_model = self.client.get_registered_model(name)
        except RestException as err:
            if err.error_code == "RESOURCE_DOES_NOT_EXIST":
                raise ModelNotRegistered(name)
            else:
                raise err
        return registered_model

    def get_latest_version(self, name: str, stage: str = "None") -> ModelVersion:
        """Get latest version of a model "name"."""
        latest_version = None
        registered_model = self.check_model_registered(name)

        for mv in registered_model.latest_versions:
            if mv.current_stage == stage:
                latest_version = mv
                break
        if latest_version is not None:
            return latest_version
        else:
            # model is registered, but no versions on stage
            raise NoVersionsOnStage(name, stage)

    def get_best_version(
        self,
        name: str,
        metric: str,
        optimal_min: bool = False,
        stage: str = "None",
    ) -> ModelVersion:
        """Get best version of model "name" according to a metric."""
        # optimal_min parameter is to look for minimal value of metric, max by default
        current_best_version, current_best_score = None, None
        self.check_model_registered(name)
        model_versions = self.client.search_model_versions(
            filter_string=f"name = '{name}'"
        )
        model_versions_on_stage = [
            mv for mv in model_versions if mv.current_stage == stage
        ]
        if not model_versions_on_stage:
            raise NoVersionsOnStage(name, stage)
        for mv in model_versions_on_stage:
            try:
                metric_value = self.client.get_run(run_id=mv.run_id).data.metrics[
                    metric
                ]
            except KeyError:
                continue  # metric might not be logged for SOME versions, so don't raise straight away

            if current_best_score is None:
                current_best_version, current_best_score = mv, metric_value
            else:
                if optimal_min:
                    if metric_value < current_best_score:
                        current_best_version, current_best_score = mv, metric_value
                else:
                    if metric_value > current_best_score:
                        current_best_version, current_best_score = mv, metric_value
        if current_best_version:
            return current_best_version
        else:
            raise MetricNotLogged(name, metric)

    def get_initial_version(self, name: str, stage: str = "None") -> ModelVersion:
        """Get initial version of model "name"."""
        #  TODO need some mechanism to identify that model is initially uploaded. Only fetch minimal version for now.
        model_versions = self.get_all_versions(name)

        model_versions_on_stage = [
            mv for mv in model_versions if mv.current_stage == stage
        ]
        if not model_versions_on_stage:
            raise NoVersionsOnStage(name, stage)
        min_version = min(model_versions_on_stage, key=attrgetter("version"))
        return min_version

    def get_version(self, name: str, version: int) -> ModelVersion:
        """
        Get model version from MLflow Model Registry and return its ModelVersion object.

        https://mlflow.org/docs/latest/python_api/mlflow.entities.html#mlflow.entities.model_registry.ModelVersion

        Parameters:
            name (str): Model name used for model registration.
            version (int): Desired version number.

        Returns:
            ModelVersion: Desired model version

        """
        # first, check that model is registered
        self.check_model_registered(name)
        # now, try to retrieve desired version
        try:
            model_version = self.client.get_model_version(name, str(version))
        except RestException as err:
            if err.error_code == "RESOURCE_DOES_NOT_EXIST":
                # model is registered, but version is not found
                raise VersionNotFound(name, str(version))
            else:
                raise err

        return model_version

    def get_all_versions(
        self,
        name: str,
    ) -> PagedList[ModelVersion]:
        """
        Get all versions of a given model and return PagedList of ModelVersion objects.

        https://mlflow.org/docs/latest/python_api/mlflow.entities.html#mlflow.entities.model_registry.ModelVersion

        Parameters:
            name (str): Model name used for model registration.

        Returns:
            PagedList[ModelVersion]: Available model versions
        """
        self.check_model_registered(name)
        model_versions = self.client.search_model_versions(
            filter_string=f"name = '{name}'"
        )

        return model_versions

    def choose_version(
        self,
        *,
        name: str,
        stage: str = "None",
        criteria: str,  # TODO enum?
        metric: str = None,
        optimal_min: bool = False,
    ) -> ModelVersion:
        """
        Choose optimal model version from MLflow Model Registry and return its ModelVersion object.

        https://mlflow.org/docs/latest/python_api/mlflow.entities.html#mlflow.entities.model_registry.ModelVersion

        Choice is made according to specified criteria.

        Parameters:
            name (str): Model name used for model registration.
            stage (str): Stage to choose version from. Defaults to "None".
            criteria (str): Criteria to choose between model versions. Must be one of: "initial", "latest", "best".
            metric (str): Metric to use with "best" criteria. Has no effect otherwise.
            optimal_min (bool): If set to True and "best" criteria is used, then choose version with minimal
                value of "metric" (useful if metric is a loss function). Defaults to False (choose version with maximal
                value of "metric").

        Returns:
            ModelVersion: Optimal model version

        """
        # for now, return single path and no name choosing -- model name must be explicitly passed
        # TODO in the future make name resolvers and return list of paths, one per chosen name
        version_fetcher_map = {
            "initial": self.get_initial_version,
            "latest": self.get_latest_version,
            "best": partial(
                self.get_best_version,
                metric=metric,
                optimal_min=optimal_min,
            ),
        }
        if criteria == "best" and metric is None:
            raise NoMetricProvided(criteria)
        if criteria in version_fetcher_map:
            return version_fetcher_map[criteria](name=name, stage=stage)
        else:
            raise UnsupportedCriteria(criteria, list(version_fetcher_map.keys))
