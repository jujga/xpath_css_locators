from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AboutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def about_banner(self):
        return self.wait.until(EC.visibility_of_element_located(((By.CSS_SELECTOR, ".about-banner"))))

    @property
    def become_member_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button[href$='membership/']")))
    def become_member_button_click(self):
        from page_objects.membership_page import MembershipPage
        self.become_member_button.click()
        return MembershipPage(self.driver)
