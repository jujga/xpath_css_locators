import os
from time import sleep
import pytest_check as check
import pytest
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from random import randint
from selenium import webdriver
import json
import andre
редактирую в ветке learning_git
в пишармовском бранче редактирую

def test():
    from IPython.display import Image
    firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
    firefox_capabilities['devtools.selfxss.count'] = 100
    firefox_capabilities['devtools.chrome.enabled'] = True
    firefox_capabilities['velikinax'] = True
    firefox_browserx = Firefox(executable_path=GeckoDriverManager().install(),
                               desired_capabilities=firefox_capabilities)
    firefox_browserx.implicitly_wait(10)
    firefox_browserx.get('https://demo.diprella.com')
    firefox_browserx.maximize_window()
    sleep(3)
    firefox_browserx.execute_script("$(window.open('https://www.ruby-lang.org'))")
    firefox_browserx.implicitly_wait(10)
    firefox_browserx.switch_to.window(firefox_browserx.window_handles[0])

    firefox_browserx.switch_to.window(firefox_browserx.window_handles[1])
    sleep(5) #без него скриншот пустой
    png = firefox_browserx.get_screenshot_as_png()
    if not 'jujgaimg' in os.listdir():
        os.mkdir('jujgaimg')
    with open(os.path.join('jujgaimg', 'shot_all_poage.png'), 'wb') as pp:
        pp.write(png)
    Image(os.path.abspath(os.path.join("img", "python_site1.png")))


def test_2():
    import os
    from IPython.display import Image

    chrome_browser = Firefox(executable_path=GeckoDriverManager().install())
    chrome_browser.maximize_window()
    chrome_browser.get('https://www.python.org')
    png_screenshot = chrome_browser.get_screenshot_as_png()

    if not "img" in os.listdir():
        os.mkdir("img")

    with open(os.path.join("img", "python_site1.png"), "wb") as pp:
        pp.write(png_screenshot)
    chrome_browser.quit()
    Image(os.path.abspath(os.path.join("img", "python_site1.png")))
