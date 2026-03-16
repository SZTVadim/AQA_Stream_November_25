from UI_project.pages.personal_page import PersonalPage


class MyInfo(PersonalPage):
    id_user = 7
    page_url = f"/pim/viewPersonalDetails/empNumber/{id_user}"

    # селекторы
    _personal_details_selector = "//h6[text()='Personal Details']"
    _personal_details_menu_selector = "//a[text()='Personal Details']"
    _salary_menu_selector = "//*[text()='Salary']"


    # локаторы
    def personal_details_locator(self):
        return self.element(self._personal_details_selector)

    def salary_locator(self):
        return self.element(self._salary_menu_selector)

    def personal_details_menu_locator(self):
        return self.element(self._personal_details_menu_selector)

    # методы
    def open_salary(self):
        self.salary_locator().click()