import pytest

from create_product import CreateProduct
from delete_product import DeleteProduct
from get_product import GetProduct
from test.data.json_for_post import JsonForPost


@pytest.fixture
def obj_get_product():
    return GetProduct()


@pytest.fixture
def obj_create_product():
    return CreateProduct()


@pytest.fixture
def obj_delete_product():
    return DeleteProduct()


@pytest.fixture
def setup_teardown_product(id_product, obj_delete_product):
    yield id_product
    obj_delete_product.delete_product(id_product)


@pytest.fixture
def id_product(obj_create_product):
    response = obj_create_product.create_product(payload=JsonForPost.JSON_OBJ_1)
    id_product = response.json()["data"]["id"]
    return id_product


@pytest.fixture
def teardown_product(obj_create_product, obj_delete_product):
    yield obj_create_product
    obj_delete_product.delete_product(id_product=obj_create_product.id_product)
