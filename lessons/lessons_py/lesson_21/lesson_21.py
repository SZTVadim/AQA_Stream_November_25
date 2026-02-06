# Практическое задание по API-тестированию

# Установить модуль request через команду pip install requests

import requests

# def search_obj(element: int):
#     response_get1 = requests.get(url="https://practice-api-qa.herokuapp.com/api/products", headers={"accept": "*/*"})
#     response_get_json_1 = response_get1.json()
#     for obj in response_get_json_1["data"]:
#         print(obj["id"])
#         if obj["id"] == element:
#             return obj
#     return "Объект не найден"




BASE_URL = "https://practice-api-qa.herokuapp.com"
ENDPOINT = "/api/products"
HEADERS = {"accept": "*/*", "Content-Type": "application/json"}

JSON_OBJ_1 ={"name": "svs5", "description": "any", "price": 101, "quantity": 5}

response_all_get = requests.get(url=f"{BASE_URL}{ENDPOINT}", headers=HEADERS)
# print(response_all_get.status_code)
# print(response_all_get.json()["data"][0]["id"])
# print(len(response_all_get.json()["data"]))


# response_post = requests.post(url=f"{BASE_URL}{ENDPOINT}", headers=HEADERS,
#                               json=JSON_OBJ_1)
# id_product = response_post.json()["data"]["id"]
#
# print(response_post)
# print(response_post.status_code)
# print(response_post.json())
# print("Create")



# response_del = requests.delete(url=f"{BASE_URL}{ENDPOINT}/{id_product}", headers=HEADERS)
# print(response_del)
# print(response_del.status_code)
# print(response_del.json())
# print("Deleted")


# оборачиваем все в методы и добавляем ассерты
# def create_product():
#     response_post = requests.post(url=f"{BASE_URL}{ENDPOINT}", headers=HEADERS,
#                                   json=JSON_OBJ_1)
#     id_product = response_post  # ["data"]["id"]
#     return id_product

def delete_product(id_product):# .json()
    response_del = requests.delete(url=f"{BASE_URL}{ENDPOINT}/{id_product}", headers=HEADERS)
    return response_del

def get_product(id_product):
    response_get = requests.get(url=f"{BASE_URL}{ENDPOINT}/{id_product}", headers=HEADERS)
    return response_get

# id_our_product = create_product()
# print(id_our_product)
# print(get_product(id_our_product))
# print(delete_product(id_our_product))
# print(get_product(id_our_product))


def test_create_product():
    try:
        product = create_product()
        assert product.status_code == 201
        assert "id" in product.json()["data"], f"{product.json()["data"]}: expected is visible key 'id' "
        assert product.json()["data"]["id"] is not None, f"{product.json()}: expected 'id'"
        assert isinstance(product.json()["data"]["id"], int), f"{type(product.json()["data"]["id"])}: expected 'DICT'"
    finally:
        delete_product(product.json()["data"]["id"])



def test_delete_product(create_product: int):
    response_delete = delete_product(create_product)
    assert response_delete.status_code == 200
    response_get = get_product(create_product)
    assert response_get.status_code == 404


