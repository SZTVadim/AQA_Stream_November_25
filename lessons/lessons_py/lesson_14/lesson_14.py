# Функции
def circle_area(radius):
    pi = 3.14
    print(pi * radius * radius)
    return pi * radius * radius


print("0")
circle_area(3)
print("1")
circle_area(6)
print("2")


def greet_user(name="Гость"):
    print(f"Hello {name}")


greet_user("Vadim")
greet_user("Dima")
greet_user("Sveta")
greet_user()


def greet_user_(name, age):
    return f"Hello {name} {age}"
    print(f"Hello {name}")  # Эта строка не выполниться при выполнении кода, так как она идет после return


greet_user_(age=28, name="Name")


def sum_int(*args):
    print(sum(args))


sum_int(1, 2, 3, 4, 5)
sum_int()


# Условные контрукции

def check_adult(age):
    if age < 18:
        print("Доступ запрещен")
    elif age >= 18 and age <= 95:
        print("Доступ разрешен")
    else:
        print("Тебе точно это надо?")


check_adult(2)
check_adult(17)
check_adult(18)
check_adult(99)


def check_temperature(temperature):
    if temperature < 0:
        print("Мороз")
    elif temperature < 20:
        print("Прохладно")
    else:
        print("Жарко")


check_temperature(10)
check_temperature(30)
check_temperature(-30)

# Конструкция match/case
command = "pause"
match command:
    case "start":
        print("Стартуем")
    case "stop":
        print("Останавливаем")
    case "pause":
        print("Пауза")
    case _:
        print("Неизвестная команда")
