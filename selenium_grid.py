import os
import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
def test_selenium_grid_firefox():
    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    desired_capabilities['marionette'] = True

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        keep_alive = True,
        desired_capabilities=desired_capabilities
        )

    time.sleep(445)

    driver.close()
def test_selenium_grid_chrome():
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        keep_alive = True,
        desired_capabilities=webdriver.DesiredCapabilities.CHROME
        )

    time.sleep(5)

    driver.close()