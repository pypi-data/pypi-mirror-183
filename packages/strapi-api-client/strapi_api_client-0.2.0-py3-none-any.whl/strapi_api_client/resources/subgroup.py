from strapi_api_client.resources.base import BaseResource


class SubgroupResource(BaseResource):
    def get_subgroup(self, name: str):
        response = self._requestor.request(
            method='GET',
            endpoint_url=f"{self._api_url}/interests?filters[name][$eqi]={name}",
            query={'filters[name][$eqi]': name}
        )
        return response

    def create_subgroup(self, data: dict):
        response = self._requestor.request(
            method='POST',
            endpoint_url=f"{self._api_url}/interests",
            payload={'data': data}
        )
        return response

    def delete_subgroup(self, subgroup_id: int):
        response = self._requestor.request(
            method='DELETE',
            endpoint_url=f"{self._api_url}/interests/{subgroup_id}"
        )
        return response
