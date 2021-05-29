from time import sleep
import pytest
import random
import string
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from page_objects.main_page import MainPage


@pytest.fixture
def main_page(request):
    #driver = Chrome(executable_path=ChromeDriverManager().install())
    driver = Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    driver.get('https://www.python.org')

    main_page = MainPage(driver)

    def fin():
        driver.quit()

    #request.addfinalizer(fin)

    return main_page


def test_about_page(main_page):
    about_page = main_page.go_to_about_page()
    about_banner = about_page.about_banner
    assert about_banner.is_displayed(), "About Banner is not displayed"
    # about_page.search('sdfsdfdsf')
    # about_page.button_go_click()
    #жмем на about_page кнопку become a member, попадаем на страницу membership, там жмем кнопку create new account (sign up button)
    sign_up_page = about_page.become_member_button_click().sign_up_button_click()
    sign_up_page.enter_email('email@gm.gk').enter_username('юзвірь').enter_password('дер пароль')
    assert sign_up_page.email_field.get_attribute('value') == 'email@gm.gk', 'Не совпало введенное и считанное'


