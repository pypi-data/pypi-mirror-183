from semantha_sdk.api import SemanthaAPIEndpoint
from semantha_sdk.api.DomainModel import Domains
from semantha_sdk.rest.RestClient import RestClient


class Model(SemanthaAPIEndpoint):

    def __init__(self, session: RestClient, parent_endpoint: str):
        super().__init__(session, parent_endpoint)
        self.__domains = Domains(session, self._endpoint)

    @property
    def _endpoint(self):
        return self._parent_endpoint + "/model"

    @property
    def domains(self) -> Domains:
        return self.__domains
