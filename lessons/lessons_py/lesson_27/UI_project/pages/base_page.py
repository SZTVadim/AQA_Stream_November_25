from playwright.sync_api import Page


class BasePage:
    BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php"
    def __init__(self, page: Page):
        self.page = page

    def open_page(self, url):
        self.page.goto(url)