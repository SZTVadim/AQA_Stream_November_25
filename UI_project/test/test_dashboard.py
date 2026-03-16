from playwright.sync_api import expect

from UI_project.test.data.name_menu import NameMenu


class TestDashboard:
    def test_dashboard_is_visible_elements(self, dashboard):
        expect(dashboard.header_locator()).to_have_text(NameMenu.DASHBOARD)
        expect(dashboard.time_at_work_locator()).to_be_visible()
        expect(dashboard.my_actions_locator()).to_be_visible()

    def test_open_dashboard(self, dashboard_page, my_info):
        my_info.open_dashboard()
        expect(dashboard_page.header_locator()).to_have_text(NameMenu.DASHBOARD)
        expect(dashboard_page.dashboard_locator()).to_contain_class("active")