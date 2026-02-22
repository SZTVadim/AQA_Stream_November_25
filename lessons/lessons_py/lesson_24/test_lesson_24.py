# Локаторы
from playwright.sync_api import sync_playwright, expect

# Импортировать модуль playwright
# pip install playwright

# Установить браузеры для playwright
# playwright install

class TestFeistUiTest:
    def test_my_first_ui_test(self):
        with sync_playwright() as p: # Запускаем сам playwright
            browser = p.chromium.launch(headless=False, slow_mo=1000) # Запускаем браузер
            # browser = p.chromium.launch(headless=True)
            context = browser.new_context() # Создаем сессию
            page = context.new_page() # открываем страницу

            page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            page.locator("[name='username']").fill("Admin")
            page.locator("[name='password']").press_sequentially("admin123", delay=100)
            expect(page.locator("[name='username']")).to_be_visible()









