from playwright.sync_api import expect

from lessons.lessons_py.lesson_27.UI_project.pages.base_page import BasePage


class DashboardPage(BasePage):
    URL = "/dashboard/index"

    # селекторы
    header_selector = ".oxd-topbar-header-breadcrumb-module"

    # локаторы
    def header_locator(self):
        return self.page.locator(self.header_selector)

    # методы
