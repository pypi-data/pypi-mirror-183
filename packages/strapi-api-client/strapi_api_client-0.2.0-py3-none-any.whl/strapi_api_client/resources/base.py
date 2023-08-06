from abc import ABC

from strapi_api_client.requestor import Requestor


class BaseResource(ABC):
    def __init__(self, api_url: str, requestor: Requestor):
        self._requestor = requestor
        self._api_url = api_url

    @property
    def requestor(self) -> Requestor:
        return self._requestor
