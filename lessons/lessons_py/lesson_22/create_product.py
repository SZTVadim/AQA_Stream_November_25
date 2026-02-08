from base_api import BaseAPI


class CreateProduct(BaseAPI):
    def create_product(self, payload):
        response = self._request(method="POST", json=payload)
        self.id_product = response.json()["data"]["id"]
        return response
