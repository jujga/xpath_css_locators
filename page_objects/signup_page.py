from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class SignUpPage(BasePage):
    from locators.locators import SignUpPageLocators


    def __init__(self, driver):
        super().__init__(driver)

    @property
    def email_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.SignUpPageLocators.EMAIL_FIELD.get_locator()))

    @property
    def username_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.SignUpPageLocators.USERNAME_FIELD.get_locator()))
    @property
    def password_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.SignUpPageLocators.PASSWORD_FIELD.get_locator()))

    @property
    def password_again_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.SignUpPageLocators.PASSWORD_AGAIN_FIELD.get_locator()))

    @property
    def signup_button_submit(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'form>button[type="submit"]')))

    def enter_email(self, keys):
        self.email_field.send_keys(keys)
        return self

    def enter_username(self, keys):
        self.username_field.send_keys(keys)
        return self

    def enter_password(self, keys):
        self.password_field.send_keys(keys)
        return self

    def signup_button_submit_click(self):
        from work_imports.membership_page import MembershipPage

        self.signup_button_submit.click()
        #пока страницу, на которую переходим после регистрации, не сделал
        #return MembershipPage(self.driver)

