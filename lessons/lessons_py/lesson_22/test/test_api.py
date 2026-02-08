from test.data.json_for_post import JsonForPost


class TestApi:
    def test_get_product(self, setup_teardown_product, obj_get_product):
        response = obj_get_product.get_product(id_product=setup_teardown_product)
        response_json = response.json()
        assert response.status_code == 200
        assert response_json["data"]["name"] == "svs15"
        assert response_json["data"]["price"] == 101
        assert response_json["data"]["quantity"] == 5


    def test_create_product(self, teardown_product):
        response = teardown_product.create_product(payload=JsonForPost.JSON_OBJ_1)
        response_json = response.json()
        assert response.status_code == 201
        assert response_json["data"]["name"] == "svs15"
        assert response_json["data"]["price"] == 101
        assert response_json["data"]["quantity"] == 5

    def test_delete_product(self, obj_delete_product, id_product, obj_get_product):
        response = obj_delete_product.delete_product(id_product=id_product)
        assert response.status_code == 200
        response_get = obj_get_product.get_product(id_product=id_product)
        assert response_get.status_code == 404
