# Кортежи Tupple
my_tupple = (1, 2, 3, 4, 5)
print(my_tupple)
print(type(my_tupple))

my_tuple_1 = 1, 2
print(my_tuple_1)
print(type(my_tuple_1))

mixed_tuple = (1, "2", [3, 4], {5: 6})
print(mixed_tuple)
print(type(mixed_tuple))

# Доступ к элементам
print(my_tupple[0])
print(my_tupple[-1])
print(my_tupple[1:3])
print(3 in my_tupple)
print(len(my_tupple))

print(my_tupple.count(2))
print(my_tupple.index(4))

if 5 in my_tupple:
    print("Нашли")

fruits = ("apple", "banana", "cherry")
print(id(fruits))
print(id(fruits * 3))

ap, ba, _ = fruits
print(ap)
print(ba)
ap, ba = ba, ap
print(ap)
print(ba)

# Преобразование в типы данных
a = "key"
b = "value"
c = "1"
d = 1
print(int(c))
print(str(d))
new_list = list(a)
print(new_list)
print(set(new_list))
print(tuple(new_list))
print(dict(zip(a, fruits)))

fruits = list(fruits)
print(fruits)
print(type(fruits))
fruits.append("cucumber")
print(fruits)
fruits = tuple(fruits)
print(fruits)
print(type(fruits))

name = (x for x in range(5))  # не кортеж, а спефивльный объект генератор
print(name)
print(type(name))

name = tuple(x ** 2 for x in range(5))  # кортеж
print(name)
print(type(name))

chars_tuple = tuple(char.upper() for char in "python")
print(chars_tuple)

# Кортежи из одного элемента
any_list = []
print(type(any_list))
any_int = (1)
print(type(any_int))

any_tuple = ("1",)
print(type(any_tuple))

any_tuple_2 = 1,
print(type(any_tuple_2))
print(any_tuple)

coordinates = (10, 20, 30, 20, 10, 20, 40)
first, *_ = coordinates
second, *_ = coordinates
print(first)
print(second)
