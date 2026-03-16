from playwright.sync_api import Page

class BasePage:
    BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php"
    page_url = ""
    id_user = ""

    def __init__(self, page: Page):
        self.page = page

    def full_url(self):
        if self.id_user:
            return f"{self.BASE_URL}/{self.page_url}/{self.id_user}"
        else:
            return f"{self.BASE_URL}/{self.page_url}"

    def open_page(self):
        self.page.goto(self.full_url())

    def element(self, selector):
        return self.page.locator(selector)