from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def about_link(self):
        return self.driver.find_element_by_css_selector('[href="/about/"]')
    @property
    def downloads_link(self):
        return self.driver.find_element_by_css_selector('[href="/downloads/"]')

    def go_to_about_page(self):
        from page_objects.about_page import AboutPage

        self.about_link.click()
        return AboutPage(self.driver)

    @property
    def search_field(self):
        return self.wait.until(EC.visibility_of_element_located(((By.CSS_SELECTOR,'#id-search-field'))))

    def search(self, keys):
        self.search_field.send_keys(keys)
        return self

    @property
    def button_go(self):
        return self.wait.until(EC.visibility_of_element_located(((By.CSS_SELECTOR,'#submit'))))
    def button_go_click(self):
        self.button_go.click()
