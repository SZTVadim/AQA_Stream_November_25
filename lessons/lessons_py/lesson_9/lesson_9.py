# Что такое словари
student = {
    "name": "Ivan",
    "age": 20,
    "is_student": True,
    "address": {
        "city": "Omsk",
        "street": "Leninskiy",
        "number_streer": [1, 2, 3]
    }
}
# print(student)  # весь объект
# print(student["name"])  #  Выводим только имя студента
# print(student["address"]["city"])
#
# print(student["address"]["number_streer"][-1])

# Основные принципы

# for key in student.values():
# print(key)
#
# for key in student.items():
#     print(key)

# Удаление элементов
# my_dict = {"a":1, "b":2, "c":3, "d":4}
# remove_value = my_dict.pop("b")
# print(remove_value)
# print(my_dict)
# del my_dict["a"]
# print(my_dict)
# my_dict.clear()
# print(my_dict)

# Генераторы словарей
# Синтаксис: {ключ: значение for элемент in итерируемый объект}
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "d": 4}
# dict3 = {"d": 5, "e": 6}
# dict1.update(dict2)
# dict3.update(dict2)
# print(dict1)
# print(dict3)
#
# words = ["apple", "banana", "cherry"]
# length_dict = {word: len(word) for word in words}
# print(length_dict)


# words = ["Inan", "Petr", "Dima"]
# length_dict = {f"user_{i}": word for i, word in enumerate(words, start=1)}
# print(length_dict)

student["stipendia"] = True
student["any_dict"] = {"any_key": "any_value"}
print(student)
