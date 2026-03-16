
from lessons.lessons_py.test_lesson_27.UI_project.pages.base_page import BasePage


class PersonalPage(BasePage):

    # селекторы
    _header_selector = ".oxd-text--h6"
    _menu_selector = ".oxd-navbar-nav"
    _search_input_selector = "[placeholder='Search']"
    _dashboard_selector = "//span[text()='Dashboard']/.."
    _my_info_selector = "//span[text()='My Info']/.."
    _collapse_menu_button_selector = ".oxd-main-menu-button"
    _personal_menu_selector = ".oxd-userdropdown-tab"
    _help_button_selector = "//*[@class='oxd-topbar-body-nav']//button"

    # локаторы
    def header_locator(self):
        return self.element(self._header_selector)

    def menu_locator(self):
        return self.element(self._menu_selector)

    def search_input_locator(self):
        return self.element(self._search_input_selector)

    def dashboard_locator(self):
        return self.element(self._dashboard_selector)

    def my_info_locator(self):
        return self.element(self._my_info_selector)

    def collapse_menu_button_locator(self):
        return self.element(self._collapse_menu_button_selector)

    def personal_menu_locator(self):
        return self.element(self._personal_menu_selector)

    def help_button_locator(self):
        return self.element(self._help_button_selector)

    # методы

    def open_dashboard(self):
        self.dashboard_locator().click()

    def open_my_info(self):
        self.my_info_locator().click()

    def collapse_menu(self):
        self.collapse_menu_button_locator().click()

