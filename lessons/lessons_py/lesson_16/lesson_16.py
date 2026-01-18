def add(a, b):  # Функция
    return a + b


i = 0  # Переменная


class Car:  # Класс
    def __init__(self, model):  # В __init__ указываем параметры необходимые при инициализации класса Car
        self.model = model

    color = "Pink"  # Это атрибут(свойство) нашего класса

    def voice(self):  # Это метод нашего класса
        print("Бип-бип")

    def privod(self):  # Это метод нашего класса
        print(f"у машины {self.model}: полный привод")


my_car = Car("Volvo")  # Это экземпляр класса Car

print(my_car.color)
print(my_car.model)
my_car.voice()
my_car.privod()
