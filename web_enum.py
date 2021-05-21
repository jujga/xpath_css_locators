from enum import Enum
import pytest
import random
import string
from time import sleep
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Helper function
def get_random_string(size=10):
    return ''.join(random.choices([*string.ascii_letters, *string.digits], k=size))


class Config(object):
    browser = None
    username = get_random_string()
    password = get_random_string()
    email = f"{get_random_string()}@gmail.com"


class WebElements(Enum):
    MEMBERSHIP_BUTTON = (By.CSS_SELECTOR, "a.button[href$='membership/']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "a.button[href$='signup/']")
    EMAIL_FIELD = (By.ID, "id_email")
    USERNAME_FIELD = (By.ID, "id_username")
    PASSWORD_FIELD = (By.ID, "id_password1")
    PASSWORD_CONFIRMATION_FIELD = (By.ID, "id_password2")
    SIGNUP_FORM_BUTTON = (By.XPATH, "//button[contains(text(), 'Sign Up')]")
    VERIFICATION_MESSAGE = (By.CSS_SELECTOR, "div.user-feedback>p[role=general]")

    def __init__(self, location_strategy, locator):
        self.location_strategy = location_strategy
        self.locator = locator

    def get(self):
        return Config.browser.find_element(self.location_strategy, self.locator)


@pytest.fixture(scope='module', autouse=True)
def browser(request):
    Config.browser = Chrome(executable_path=ChromeDriverManager().install())
    Config.browser.maximize_window()
    Config.browser.get('https://www.python.org')

    request.addfinalizer(Config.browser.quit)


def test_register_membership():
    WebElements.MEMBERSHIP_BUTTON.get().click()
    WebElements.SIGNUP_BUTTON.get().click()
    WebElements.EMAIL_FIELD.get().send_keys(Config.email)
    WebElements.USERNAME_FIELD.get().send_keys(Config.username)
    WebElements.PASSWORD_FIELD.get().send_keys(Config.password)
    WebElements.PASSWORD_CONFIRMATION_FIELD.get().send_keys(Config.password)
    WebElements.SIGNUP_FORM_BUTTON.get().click()

    WebElements.

    expected_verification_message = f"Confirmation e-mail sent to {Config.email}."
    actual_verification_message = WebElements.VERIFICATION_MESSAGE.get().text

    assert actual_verification_message == expected_verification_message, f"Unexpected verification message: {actual_verification_message}.\
  Should be: {expected_verification_message}"
