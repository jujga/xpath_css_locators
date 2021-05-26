from selenium.webdriver.common.by import By
from enum import Enum
from fixtures import browser, Config
class WebElements(Enum):
    REGISTER_BUTTON = '//div[@class = "header__nav-button"]'
    CHECK_BOX_I_HAVE_READ = '//label[@class = "terms"]'
    INP_NAME = '//input[@formcontrolname = "first_name"]'
    INP_FAMILY = '//input[@formcontrolname = "last_name"]'
    INP_EMAIL = '//input[@formcontrolname = "email"]'
    INP_PASSW = '//input[@formcontrolname = "password"]'
    SUBMIT_BTT = '//button[contains(@class,"login__form-btn")]'

    PROFILE_LINK = '//nav[@class="navigate-bar__nav"]/a[contains(@class, "ng-star-inserted")]'
    LOGO_LINK = '//div[@class = "header__logo"]'
    LIBRARY = '//div[@class = "library"]'

    def __init__(self, locator):
        #self.strategy = strategy
        self.locator = locator
    def get(self):
        return Config.browser.find_element(By.XPATH, self.locator)
    @property
    def strategy_locator(self):
        return (By.XPATH, self.locator)
