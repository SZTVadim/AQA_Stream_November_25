from playwright.sync_api import expect

from UI_project.test.data.name_menu import NameMenu


class TestMyInfo:
    def test_my_info_is_visible_elements(self, my_info):
        expect(my_info.header_locator()).to_have_text(NameMenu.MY_INFO)
        expect(my_info.personal_details_locator()).to_be_visible()
        expect(my_info.personal_details_menu_locator()).to_be_visible()
        expect(my_info.salary_locator()).to_be_visible()

    def test_open_my_info(self, dashboard, my_info_page):
        dashboard.open_my_info()
        expect(my_info_page.header_locator()).to_have_text(NameMenu.MY_INFO)
        expect(my_info_page.my_info_locator()).to_contain_class("active")

