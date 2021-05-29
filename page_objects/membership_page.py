from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MembershipPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def sign_up_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button[href$='/accounts/signup/']")))

    def sign_up_button_click(self):
        from page_objects.signup_page import SignUpPage
        self.sign_up_button.click()
        return SignUpPage(self.driver)
