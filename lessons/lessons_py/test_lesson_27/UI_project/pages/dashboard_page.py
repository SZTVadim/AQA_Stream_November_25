from lessons.lessons_py.test_lesson_27.UI_project.pages.personal_page import PersonalPage


class DashboardPage(PersonalPage):
    page_url = "/dashboard/index"

    # селекторы
    _time_at_work_selector = "//*[text()='Time at Work']/../../.."
    _my_actions_selector = "//*[text()='My Actions']/../../.."


    # локаторы
    def time_at_work_locator(self):
        return self.element(self._time_at_work_selector)

    def my_actions_locator(self):
        return self.element(self._my_actions_selector)
    # методы
