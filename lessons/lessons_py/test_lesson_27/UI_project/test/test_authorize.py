from time import sleep

from playwright.sync_api import expect


class TestAuthorize:
    def test_login(self, auth_page, dashboard_page):
        auth_page.open_page()
        expect(auth_page.page).to_have_title("OrangeHRM")
        # sleep(2)
        expect(auth_page.header_locator()).to_be_visible()
        expect(auth_page.header_locator()).to_have_text("Login")
        # sleep(2)
        expect(auth_page.submit_locator()).to_have_css("background-color", "rgb(255, 123, 29)")
        # auth_page.authorize("Admin", "admin123")
        # sleep(2)
        # expect(dashboard_page.header_locator()).to_have_text("Dashboard")
        # sleep(2)