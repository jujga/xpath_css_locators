from time import sleep
import pytest
from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
# @pytest.fixture
# def browser(request):
#
#     driver = Firefox(executable_path=GeckoDriverManager().install())
#     driver.maximize_window()
#     driver.get('about:config')
#     driver.implicitly_wait(5)
#
#
#     def fin():
#         driver.quit()
#
#     #request.addfinalizer(fin)
#
#     return driver

def about_conf_ins_allow(browser):
    browser.get('about:config')
    browser.implicitly_wait(5)
    browser.find_element_by_css_selector('#warningButton').click()
    browser.find_element_by_css_selector('#about-config-search').send_keys('devtools.chrome.enabled')
    actions = action_chains.ActionChains(browser)
    row_to_doubleclick = browser.find_element_by_css_selector('table#prefs')
    actions.double_click(row_to_doubleclick).perform()

    #browser.close() #закрываем текущую вкладку с настройками
    #actions.key_down(Keys.CONTROL).send_keys('W').perform()
    #browser.switch_to.window(browser.window_handles[0])
    # чтобы заработала browser.close, нужно после него влупить переключение на новую вкладку,
    # что образовалась после закрытия старой, и сделать ретурн драйвера
    #browser.find_element_by_css_selector("button.button-toggle").click()
    #firefox_capabilities['devtools.selfxss.count'] = 100
    #firefox_capabilities['devtools.chrome.enabled'] = True
    #return browser