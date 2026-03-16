import pytest
from playwright.sync_api import sync_playwright, Page

from UI_project.pages.auth_page import AuthPage
from UI_project.pages.dashboard_page import DashboardPage
from UI_project.pages.my_info_page import MyInfo
from UI_project.pages.reset_password import ResetPasswordPage
from UI_project.test.data.authorize_data import AuthorizeData


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="function")
def browser(playwright_instance, request):
    browser = playwright_instance.chromium.launch(headless=False, slow_mo=500)
    # browser = playwright_instance.chromium.launch()
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    browser.close()


@pytest.fixture(scope="function")
def page(context) -> Page:
    page: Page = context.new_page()
    return page


@pytest.fixture
def auth_page(page):
    return AuthPage(page)


@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)


@pytest.fixture
def reset_password_page(page):
    return ResetPasswordPage(page)


@pytest.fixture
def my_info_page(page):
    return MyInfo(page)


@pytest.fixture
def dashboard(auth_page, dashboard_page):
    auth_page.open_page()
    auth_page.authorize(AuthorizeData.LOGIN, AuthorizeData.PASSWORD)
    return dashboard_page


@pytest.fixture
def my_info(dashboard, my_info_page):
    dashboard.open_my_info()
    return my_info_page
