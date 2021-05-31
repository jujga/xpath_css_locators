import pytest
from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
@pytest.fixture
def browser(request):

    driver = Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    driver.get('about:config')
    driver.implicitly_wait(5)


    def fin():
        driver.quit()

    #request.addfinalizer(fin)

    return driver

def test_ab_conf(browser):
    browser.find_element_by_css_selector('#warningButton').click()
    browser.find_element_by_css_selector('#about-config-search').send_keys('dsfsdf')