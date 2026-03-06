# age = 27
# def age_():
#     return 27
# 
# class Parent:
#     eyes = "blue"
# 
#     def sound(self):
#         pass
# 
# 
# dad = Parent()
# print(dad.eyes)
from playwright.sync_api import Page


class BasePage(Page):
    BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php"
    page = Page
    # селекторы
    login_selector = ".login"
    password_selector = ".password"
    auth_selector = ".auth_button"
    
    # локаторы
    
    login_locator = page.locator(".login")
    password_locator = page.locator(password_selector)
    auth_locator = page.locator(auth_selector)



    
    