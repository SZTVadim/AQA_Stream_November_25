# Декораторы
import datetime
import random
import time
from time import sleep


def any_name_decorator(func):
    def wrapper():
        print("Начало выполнения функции")
        func()
        print("Конец выполнения функции")

    return wrapper


@any_name_decorator
def greeting():
    print(f"Hello ")


# greeting()


def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                a = time.time()
                func(*args, **kwargs)
                b = time.time()
                print(b - a)
                print("=" * 80)
        return wrapper
    return decorator_repeat

@repeat(num_times=5)
def say_hello(name):
    sleep(random.randint(1, 3))
    print(f"Привет, {name}!")

# say_hello("Анна")


class Employee:
    company = "TechCorp"  # Обычная переменная класса (общая для всех объектов)

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        # Обычный метод - работает с конкретным объектом (self)
        print(f"{self.name} зарабатывает {self.salary} в компании {self.company}")

    @classmethod
    def change_company(cls, new_company):
        # Метод класса - работает с классом в целом (cls)
        cls.company = new_company
        print(f"Название компании изменено на: {new_company}")

    @classmethod
    def from_string(cls, employee_string):
        # Ещё один полезный пример - альтернативный конструктор
        name, salary = employee_string.split("-")
        return cls(name, int(salary))

# Создаем объекты
emp1 = Employee("Иван", 50000)
emp2 = Employee("Мария", 60000)


# Используем обычный метод
emp1.display_info()  # Иван зарабатывает 50000 в компании TechCorp
emp2.display_info()
print("=" * 80)

# Используем метод класса - меняем компанию для ВСЕХ объектов
Employee.change_company("NewTech")

# Теперь все объекты используют новое название компании
emp1.display_info()  # Иван зарабатывает 50000 в компании NewTech
emp2.display_info()  # Мария зарабатывает 60000 в компании NewTech
# Используем альтернативный конструктор
emp3 = Employee.from_string("Петр-70000")
emp3.display_info()# Петр зарабатывает 70000 в компании NewTech
print(emp3.company)
print(emp3.salary)

# @staticmethod

class Vehicle:
    __name = "Motorcycle"
    @staticmethod
    def is_motorcycle(wheels):
        return wheels == 2

    @property
    def name_moto(self):
        return {self.__name}



print(Vehicle.is_motorcycle(3))  # False
print(Vehicle.is_motorcycle(2)) # True
v = Vehicle()
print(v.name_moto)