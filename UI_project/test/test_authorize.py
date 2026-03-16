from time import sleep

from playwright.sync_api import expect

from UI_project.test.data.authorize_data import AuthorizeData
from UI_project.test.data.name_menu import NameMenu
from UI_project.test.data.title_name import TitleName


class TestAuthorize:
    def test_login(self, auth_page, dashboard_page):
        auth_page.open_page()
        auth_page.authorize(AuthorizeData.LOGIN, AuthorizeData.PASSWORD)
        sleep(3)
        expect(dashboard_page.header_locator()).to_have_text(NameMenu.DASHBOARD)

    def test_is_visible_elements(self, auth_page):
        auth_page.open_page()
        expect(auth_page.header_locator()).to_be_visible()
        expect(auth_page.login_locator()).to_be_visible()
        expect(auth_page.password_locator()).to_be_visible()
        expect(auth_page.submit_locator()).to_be_visible()
        expect(auth_page.forgot_password_locator()).to_be_visible()
        sleep(3)


    def test_invalid_login(self, auth_page):
        auth_page.open_page()
        auth_page.authorize(AuthorizeData.PASSWORD, AuthorizeData.PASSWORD)
        expect(auth_page.alert_locator()).to_be_visible()
        sleep(3)


    def test_invalid_password(self, auth_page):
        auth_page.open_page()
        auth_page.authorize(AuthorizeData.LOGIN, AuthorizeData.LOGIN)
        expect(auth_page.alert_locator()).to_be_visible()
        sleep(3)


    def test_emty_login(self, auth_page):
        auth_page.open_page()
        auth_page.authorize(password=AuthorizeData.PASSWORD)
        expect(auth_page.error_message_login_locator()).to_be_visible()
        expect(auth_page.error_message_login_locator()).to_have_text("Required")
        sleep(3)


    def test_emty_password(self, auth_page):
        auth_page.open_page()
        auth_page.authorize(AuthorizeData.LOGIN)
        expect(auth_page.error_message_password_locator()).to_be_visible()
        expect(auth_page.error_message_password_locator()).to_have_text("Required")
        sleep(3)


    def test_click_lick_on_official_site(self, auth_page, context):
        auth_page.open_page()
        with context.expect_page() as context_event:
            auth_page.link_official_site_locator().click()
        new_page = context_event.value
        expect(new_page).to_have_title(TitleName.OFFICIAL_SITE)
