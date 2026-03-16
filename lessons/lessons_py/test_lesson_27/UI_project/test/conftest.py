import pytest
from playwright.sync_api import sync_playwright, Page

from lessons.lessons_py.test_lesson_27.UI_project.pages.auth_page import AuthPage
from lessons.lessons_py.test_lesson_27.UI_project.pages.dashboard_page import DashboardPage
from lessons.lessons_py.test_lesson_27.UI_project.pages.my_info_page import MyInfo
from lessons.lessons_py.test_lesson_27.UI_project.pages.reset_password import ResetPasswordPage


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def browser(playwright_instance, request):
    # browser = playwright_instance.chromium.launch(headless=False, slow_mo=50)
    browser = playwright_instance.chromium.launch()
    yield browser
    browser.close()

@pytest.fixture(scope="session")
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