# Множества

numbers = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
print(numbers)
print(len(numbers))
print(3 in numbers)

# Преобразование других типов данных в множество
numbers = [1, 4, 2, 2, 3, 3, 4]
unique_value = set(numbers)
print(unique_value)

text = "Hello world"
unique_letter = set(text)
print(unique_letter)
my_tupple = (1, 4, 2, 2, 3, 3)
print(my_tupple)
set_with_tupple = set(my_tupple)
print(set_with_tupple)

# Добавление элементов
fruits = {"apple", "banana", "cherry"}
print(f" ID до преобразования {id(fruits)}")
fruits.add("orange")
fruits.add("orange")
print(fruits)

fruits_2 = {"яблоко", "банан", "вишня"}
fruits.update(fruits_2)
print(f" ID до преобразования {id(fruits)}")
print(sorted(fruits, reverse=True))
print(sorted(list(fruits)))

# Удаление элементов
fruits = {"яблоко", "банан", "апельсин", "мандарин", "клубника"}
fruits.discard("банан")
print(fruits)
fruits.remove("яблоко")
# fruits.remove("банан")  # Вызовет ошибку, так как пытаемся удалить удаленый элемент
print(fruits)
deleting_fruits = fruits.pop()
print(deleting_fruits)
print(fruits)
