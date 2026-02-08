import requests


class BaseAPI:
    BASE_URL = "https://practice-api-qa.herokuapp.com"
    ENDPOINT = "/api/products"
    HEADERS = {"accept": "*/*", "Content-Type": "application/json"}
    id_product = ""
    def _request(self, method: str, id_product: str =None, **kwargs):
        if id_product:
            url = f"{self.BASE_URL}{self.ENDPOINT}/{id_product}"
        else:
            url = f"{self.BASE_URL}{self.ENDPOINT}"
        response = requests.request(method, url, headers=self.HEADERS, **kwargs)
        return response
