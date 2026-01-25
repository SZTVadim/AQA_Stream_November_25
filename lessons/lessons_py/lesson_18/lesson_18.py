# ООП


class Parent:
    def __init__(self, name, age_year):
        self.name = name
        self.age_year = age_year  # Год рождения

    color_eyes = "blue"


class Child(Parent):
    def __init__(self, name, age_year):
        super().__init__(name, age_year)

    child = True

    def sound(self):
        return "Мои родители теперь бабушка и дедушка"


class Grandson(Child):
    def __init__(self, name, age_year):
        super().__init__(name, age_year)

    def sound(self):
        return "Агу"


# print(Child("Boby", 18).color_eyes)
# adult = Parent("John", "44").color_eyes
# time = datetime.datetime.time(datetime.datetime.now())
# print(time)
# print(Child("Boby", 18).sound())
# print(Grandson("Boby", 2).sound())
# print(Grandson("Boby", 18).color_eyes)

# from abc import ABC, abstractmethod
#
# class Car_1(ABC):
#     @abstractmethod
#     def start_engine(self):
#         """
#         Абстрактный метод для запуска двигателя.
#         Должен быть переопределён в подклассах.
#         """
#         pass
#     @staticmethod
#     def stop_engine():
#         """
#         Обычный метод (не абстрактный) — его можно переопределить,
#         но не обязательно. По умолчанию двигатель просто останавливается.
#         """
#         print("Двигатель остановлен.")
#
# class Toyota(Car_1):
#     def start_engine(self):
#         print("Запуск по ключу")

#
# car = Toyota()
# car.start_engine()
# car.stop_engine()


class Car:
    def __init__(self, brand, model, fuel_level=0):
        self.brand = brand
        self.model = model
        self.__fuel_level = fuel_level  # Приватный атрибут, не доступный напрямую

    def refuel(self, amount):
        """Метод для заправки автомобиля"""
        if amount > 0:
            self.__fuel_level += amount
            if self.__fuel_level > 100:  # Предположим, что уровень топлива не может превышать 100%
                self.__fuel_level = 100
            print(f"{self.brand} {self.model}: Добавлено {amount}% топлива. Текущий уровень: {self.__fuel_level}%.")
        else:
            print("Сумма для заправки должна быть положительной!")

    def drive(self, consumption):
        """Метод для симуляции поездки, во время которой расходуется топливо"""
        if consumption > self.__fuel_level:
            print(f"{self.brand} {self.model}: Недостаточно топлива для поездки!")
        else:
            self.__fuel_level -= consumption
            print(f"{self.brand} {self.model}: Поездка завершена. Осталось {self.__fuel_level}% топлива.")

    def get_fuel_level(self):
        """Метод для получения текущего уровня топлива"""
        return self.__fuel_level


my_car = Car("Honda", "Civic", fuel_level=50).get_fuel_level()
