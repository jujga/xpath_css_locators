from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def membership_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button[href$='membership/']")))

    def click_membership_button(self):
        from work_imports.membership_page import MembershipPage

        self.membership_button.click()

        return MembershipPage(self.driver)

