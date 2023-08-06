from rhino_health.lib.endpoints.endpoint import Endpoint
from rhino_health.lib.endpoints.model_result.model_result_dataclass import ModelResult
from rhino_health.lib.utils import rhino_error_wrapper


class ModelResultEndpoints(Endpoint):
    @property
    def model_result_data_class(self):
        """
        @autoapi False
        """
        return ModelResult


class ModelResultFutureEndpoints(ModelResultEndpoints):
    @rhino_error_wrapper
    def get_model_result(self, model_result_uid: str):
        """
        Returns a ModelResult dataclass

        Parameters
        ----------
        model_result_uid: str
            UID for the ModelResult

        Returns
        -------
        model_result: ModelResult
            ModelResult dataclass

        Examples
        --------
        >>> session.aimodel.get_model_result(model_result_uid)
        ModelResult()
        """
        result = self.session.get(f"/federatedmodelactions/{model_result_uid}")
        return result.to_dataclass(self.model_result_data_class)
