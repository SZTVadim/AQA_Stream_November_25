import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page

from lessons.lessons_py.lesson_27.UI_project.pages.auth_page import AuthPage
from lessons.lessons_py.lesson_27.UI_project.pages.dashboard_page import DashboardPage


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

@pytest.fixture(scope="function")
def page(browser: Browser) -> Page:
    context: BrowserContext = browser.new_context()
    page: Page = context.new_page()
    return page


@pytest.fixture
def auth_page(page):
    return AuthPage(page)

@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)
