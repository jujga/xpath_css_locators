from enum import Enum
from selenium.webdriver.common.by import By


class SignUpPageLocators(Enum):
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_email")
    USERNAME_FIELD = (By.CSS_SELECTOR, '#id_username')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_password1')
    PASSWORD_AGAIN_FIELD = (By.CSS_SELECTOR, '#id_password2')

    def __init__(self, strategy, locator):
        self.strategy = strategy
        self.locator = locator

    def get_locator(self):
        return (self.strategy, self.locator)
