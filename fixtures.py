import pytest
from selenium.webdriver import Firefox

from webdriver_manager.firefox import GeckoDriverManager

from selenium import webdriver



class Config:
    browser = None

@pytest.fixture(scope='module', autouse=True)
def browser():
    firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
    #firefox_capabilities['devtools.selfxss.count'] = 100
    #firefox_capabilities['devtools.chrome.enabled'] = True
    Config.browser = Firefox(executable_path=GeckoDriverManager().install())#, desired_capabilities=firefox_capabilities)
    Config.browser.implicitly_wait(5)
    Config.browser.get('https://demo.diprella.com')
    Config.browser.maximize_window()