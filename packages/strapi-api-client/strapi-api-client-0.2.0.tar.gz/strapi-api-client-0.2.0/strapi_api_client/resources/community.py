from strapi_api_client.resources.base import BaseResource


class CommunityResource(BaseResource):
    def get_community(self, name: str):
        response = self._requestor.request(
            method='GET',
            endpoint_url=f"{self._api_url}/communities?filters[name][$eqi]={name}",
            query={'filters[name][$eqi]': name}
        )
        return response

    def create_community(self, data: dict):
        response = self._requestor.request(
            method='POST',
            endpoint_url=f"{self._api_url}/communities",
            payload={'data': data}
        )
        return response

    def delete_community(self, community_id: int):
        response = self._requestor.request(
            method='DELETE',
            endpoint_url=f"{self._api_url}/communities/{community_id}"
        )
        return response
