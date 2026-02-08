from base_api import BaseAPI


class DeleteProduct(BaseAPI):
    def delete_product(self, id_product):  # .json()
        response_del = self._request(method="DELETE", id_product=id_product)
        return response_del
