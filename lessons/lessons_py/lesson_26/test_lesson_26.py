# pip install pytest-playwright
from time import sleep

from playwright.sync_api import Page, expect, BrowserContext, Dialog


def test_visible(page: Page):
    page.goto("https://www.qa-practice.com/elements/input/simple")
    reqs = page.locator("#req_text")
    expect(reqs).not_to_be_visible()
    expect(reqs).to_be_hidden()
    sleep(3)
    page.locator("#req_header").click()
    expect(reqs).to_be_visible()
    sleep(2)

def test_enabled_and_select(page: Page):
    sleep(3)
    page.goto("https://www.qa-practice.com/elements/button/disabled")
    button = page.locator("#submit-id-submit")
    expect(button).to_be_disabled()
    sleep(2)
    page.locator("#id_select_state").select_option("Enabled")
    sleep(2)
    expect(button).to_be_enabled()
    expect(button).to_have_text("Submit")
    expect(button).to_contain_text("mit")
    sleep(3)

def test_value_input(page: Page):
    text = "qwerty"
    page.goto("https://www.qa-practice.com/elements/input/simple")
    input_field = page.locator("#id_text_string")
    sleep(4)
    # input_field.fill(text)
    input_field.press_sequentially(text, delay=500)
    # sleep(3)
    expect(input_field).to_have_value(text)
    input_field.press("Enter")
    sleep(2)
    result_text = page.locator("#result-text")
    expect(result_text).to_be_visible()


def test_focus(page: Page):
    page.goto("https://www.google.com/")
    field = page.locator("[name='q']")
    page.locator("//div[contains(@class, 'qarstb')]").click()
    expect(field).not_to_be_focused()
    field.focus()
    expect(field).to_be_focused()

def test_tabs(page: Page, context: BrowserContext):
    sleep(3)
    page.goto("https://www.qa-practice.com/elements/new_tab/link")
    link = page.locator("#new-page-link")
    with context.expect_page() as new_page_event:
        link.click()
    sleep(3)
    new_page = new_page_event.value
    result_text = new_page.locator("#result-text")
    expect(result_text).to_have_text("I am a new page in a new tab")
    new_page.close()
    page.get_by_role("link", name="New tab button").click()
    sleep(3)

def test_d_n_d(page: Page):
    page.goto("https://www.qa-practice.com/elements/dragndrop/boxes")
    drag_me = page.locator("#rect-draggable")
    drag_here = page.locator("#rect-droppable")
    sleep(4)
    drag_me.drag_to(drag_here)
    sleep(2)
    dropped = page.locator("#text-droppable")
    expect(dropped).to_have_text("Dropped!")


def test_alert_box(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/alert#")

    def hadler_accept(alert: Dialog):
        sleep(2)
        alert.accept()

    page.on("dialog", hadler_accept)
    page.locator(".a-button").click()

def test_alert_dismiss(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm")

    def hadler_dismiss(alert: Dialog):
        sleep(2)
        alert.dismiss()

    page.on("dialog", hadler_dismiss)
    page.locator(".a-button").click()
    sleep(2)
    expect(page.locator("#result-text")).to_have_text("Cancel")

def test_alert_promt(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/prompt")
    text = "Hello"

    def hadler_accept(alert: Dialog):
        sleep(2)
        alert.accept(text)

    page.on("dialog", hadler_accept)
    page.locator(".a-button").click()
    sleep(2)
    expect(page.locator("#result-text")).to_have_text(text)