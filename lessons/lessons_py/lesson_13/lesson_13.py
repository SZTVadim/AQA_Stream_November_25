data = [1, 2, 4]
one, two, four = data
# print(one)
# print(two)
# print(four)

data_1 = [1, 2, 3, 4, 5]
a, *_, v, c = data_1
print(a)
# print(b)
print(c)
print(v)

user = ("John", "Doe", 28, "teacher", 150000)
# name, surname, age, position, salary = user
*_, position, salary = user
# print(name)
# print(user)
# print(age)
print(position)
print(salary)

my_set = {"Vasya", "4", "ерунда"}
my_set1 = {100, 200, 300}  # по особенному работает с цмфрами
a, b, c = my_set
# print(type(my_set))
print(a)
print(b)
print(c)

student = {"имя": "Иван", "возраст": 20, "город": "Москва"}
for key, value in student.items():
    print(f"{key}, {value}")


def greet(name, age):
    print(f"Hello, {name}, {age}")


user = {"name": "Иван", "age": 23}

greet("Вася", 99)

greet(**user)


def sum_func(a, b, c):
    return a + b + c


numbers = [1, 2, 3]

my_sum = sum_func(*numbers)
print(my_sum)


def process_data(*args, **kwargs):
    print(f"Позиционные аргументы: {args}")
    print(f"Именные аргументы: {kwargs}")
    print(f"Всего позиционных: {len(args)}")
    print(f"Всего именованных: {len(kwargs)}")


process_data(name="Иван", age=23)
