import pytest
import requests

from lessons.lessons_py.lesson_21.lesson_21 import BASE_URL, ENDPOINT, JSON_OBJ_1, HEADERS


@pytest.fixture
def create_product():
    response_post = requests.post(url=f"{BASE_URL}{ENDPOINT}", headers=HEADERS,
                                  json=JSON_OBJ_1)
    id_product = response_post.json()["data"]["id"]
    print(id_product)
    return id_product
