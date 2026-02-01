# импортирвоание модулей
import math  # математический модуль

import pytest  # фреймворк для тестирования
import requests  # фреймворт для запрсоов API

from lessons.lessons_py.lesson_20.utils.randomayzer import Randomiz  # Модуль для получения рандомных значений


a = math.pi
print(a)
random_int = Randomiz().get_random_int()
print(random_int)


# assert random_int == 55, f"Ты не угадал {random_int} не 55"  # assert встроенный инструмент для проверок

"""Метод POST с невалидными данными, его не запускать"""
# data = {"key": "value"}
# response = requests.post("https://petstore.swagger.io/v2/pets?status=sold", json=data, headers={"accept": "application/json"})
# print(response.json())

"""Метод POST с невалидными данными, его не запускать"""
# response_get_any = requests.get("https://petstore.swagger.io/v2/pet/665", headers=headers)
# print(response)
# print(response.status_code)
# print(response.text)
# print(response_get_any.json()["category"]["name"])
# print(response_get_any.json())

# assert response.json()["category"]["name"] == "SVS"  # Проверка структуры ответа на наличие данных, так как данные кривые, првоерка падает
headers_for_get = {"accept": "application/json"}
headers_for_post = {"accept": "application/json", "Content-Type": "application/json"}
data_for_post = {
  "id": 667,
  "category": {
    "id": 0,
    "name": "SVS"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

"""Создаем запись"""
response_post_any = requests.post("https://petstore.swagger.io/v2/pet", headers=headers_for_get, json=data_for_post)
print(f"{response_post_any.status_code}, успешно создан")
print(response_post_any.json())

"""Получаем запись запись"""
response_post = requests.get("https://petstore.swagger.io/v2/pet/667", headers=headers_for_post)
print(f"{response_post.status_code}, успешно получен")


"""Удаляем запись"""
response_delete_any = requests.delete("https://petstore.swagger.io/v2/pet/667", headers=headers_for_get)
print(f"{response_delete_any.status_code}, успешно удален")
print(response_delete_any.json())


"""Наша первая фикстура """
@pytest.fixture
def setup_teardown():  # setup это предусловие
  response_post = requests.post("https://petstore.swagger.io/v2/pet", json=data_for_post, headers=headers_for_post)
  print(f"{response_post.status_code}, успешно создан")
  id_animal = response_post.json()["id"]
  yield id_animal
  response_delete = requests.delete(f"https://petstore.swagger.io/v2/pet/{id_animal}", headers=headers_for_get)  # teardown это предусловие
  print(f"{response_delete.status_code}, успешно удален")

"""Наш первый автотест, запускать его через зеленую кнопочку или через терминал "команда"
 pytest <Путь к фпйлу от корня репозитория pytest>   
  - PS. символы <ставить не надо>
  - Переименовать локально файл в test_lesson_20.py"""
def test_get_pet_by_id(setup_teardown):
  response_get = requests.get(f"https://petstore.swagger.io/v2/pet/{setup_teardown}", headers=headers_for_get)
  print(f"{response_get.status_code}, гет отработал")
  print(f"{response_get.json()}")
  assert response_get.status_code == 200

