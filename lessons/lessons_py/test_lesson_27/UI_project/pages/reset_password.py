from lessons.lessons_py.test_lesson_27.UI_project.pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    page_url = "/auth/requestPasswordResetCode"
    # селекторы
    _header_fp_selector = ".orangehrm-forgot-password-title"
    _username_input_selector = "[placeholder='Username']"
    _reset_password_button_selector = ".oxd-button--secondary"
    # локаторы
    def header_fp_locator(self):
        self.element(self._header_fp_selector)

    def username_input_locator(self):
        self.element(self._username_input_selector)

    def reset_password_button_locator(self):
        self.element(self._reset_password_button_selector)
    # методы

