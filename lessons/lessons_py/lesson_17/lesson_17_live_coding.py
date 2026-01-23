# Задание 1: Класс для тестовых данных пользователя
# Задача:
# Создайте класс TestUser для хранения и работы с данными пользователя в тестах. Класс должен
# позволять создавать пользователей с различными данными и валидировать их корректность.

# Требования:
# 1. (Sveta) Класс должен иметь конструктор __init__, который принимает:
#    - username (обязательный)
#    - email (обязательный)
#    - password (обязательный)
#    - age (опциональный, по умолчанию None)
#    - is_active (опциональный, по умолчанию True)

class TestUser:
    def __init__(self, username, email, password, age=None, is_active=False):
        self.username = username
        self.email = email
        self.password = password
        self.age = age
        self.is_active = is_active

    # 2. (Ramil) Добавьте метод validate_email(), который проверяет, что email содержит символ "@"
    #    и возвращает True/False
    def validate_email(self):
        return "@" in self.email

    # 3. (Dmitry R)Добавьте метод validate_password(), который проверяет, что пароль содержит минимум
    #    8 символов и возвращает True/False
    def validate_password(self):
        if len(self.password) >= 8:
            return True
        else:
            False
        # return len(self.password) >= 8. # Можно использовать более короткое написание

    # 4.(Vadim) Добавьте метод get_user_info(), который возвращает словарь со всеми данными пользователя
    def get_user_info(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "age": self.age,
            "is_active": self.is_active
        }

    # 5.(D) Добавьте метод is_adult(), который возвращает True, если возраст >= 18, иначе False
    #    (если возраст не указан, возвращает None)
    def is_adult(self):
        if self.age is None:
            return None
        return self.age >= 18

    def new_age(self, new_age_value):
        self.age = int(input())


new_user = TestUser("Vova", "email@email.com", "passw")
print(new_user.password)
print(new_user.get_user_info())
new_user1 = TestUser("Dima", "123@email.ru", "qwe123qwe", 30, True)
print(id(new_user1))
print(new_user1.is_adult())

print(new_user1.age)
new_user1.new_age(55)
print(new_user1.age)
print(new_user1.get_user_info())
