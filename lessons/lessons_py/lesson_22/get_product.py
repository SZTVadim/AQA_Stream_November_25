from base_api import BaseAPI


class GetProduct(BaseAPI):
    def get_product(self, id_product: str):
        return self._request(method="GET", id_product=id_product)
