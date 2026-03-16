import allure

from lessons.lessons_py.test_lesson_27.UI_project.pages.base_page import BasePage


class AuthPage(BasePage):
    page_url = "/auth/login"

    # селекторы
    _header_selector = ".orangehrm-login-title"
    _login_selector = "[name='username']"
    _password_selector = "[placeholder='Password']"
    _submit_selector = "[type='submit']"
    _forgot_password_selector = ".orangehrm-login-forgot-header"

    # локаторы
    def header_locator(self):
        return self.element(self._header_selector)

    def login_locator(self):
        return self.element(self._login_selector)

    def password_locator(self):
        return self.element(self._password_selector)

    def submit_locator(self):
        return self.element(self._submit_selector)

    def forgot_password_locator(self):
        return self.element(self._forgot_password_selector)

    # методы
    @allure.step("Ввести логин")
    def fill_login(self, login):
        self.login_locator().fill(login)

    @allure.step("Ввести пароль")
    def fill_password(self, password):
        self.password_locator().fill(password)

    @allure.step("Нажать кнопку Login")
    def click_login(self):
        self.submit_locator().click()

    @allure.step("Нажать на 'Forgot your password?'")
    def click_forgot_password(self):
        self.forgot_password_locator().click()

    # Комбинированные методы
    def authorize(self, login, password):
        self.fill_login(login)
        self.fill_password(password)
        self.click_login()
