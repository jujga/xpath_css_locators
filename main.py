from time import sleep
import pytest_check as check
import pytest
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from random import randint
from selenium import webdriver
from  selenium.common import exceptions

@pytest.fixture
def firefox_browser1():
    firefox_browser1 = Firefox()
    firefox_browser1.get('https://python.org')

    yield firefox_browser1
    firefox_browser1.close()

@pytest.fixture
def firefox_browser2():
    firefox_browser2 = Firefox()
    firefox_browser2.get('https://www.joom.com/uk')

    yield firefox_browser2
    firefox_browser2.close()

@pytest.fixture
def firefox_browser3():
    #firefox_browser3 = Firefox()
    firefox_browser3 = Firefox(executable_path=GeckoDriverManager().install())
    firefox_browser3.get('https://www.joom.com/uk')

    yield firefox_browser3
    firefox_browser3.close()

@pytest.fixture
def firefox_browser4():

    firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
    firefox_capabilities['devtools.selfxss.count'] = 100
    firefox_capabilities['devtools.chrome.enabled'] = True
    firefox_browser4 = Firefox(executable_path=GeckoDriverManager().install(), desired_capabilities=firefox_capabilities)
    firefox_browser4.implicitly_wait(3)
    firefox_browser4.get('https://demo.diprella.com')
    firefox_browser4.maximize_window()
    yield firefox_browser4

    #firefox_browser4.close()


"""BR1: open python.org
BR1: navigate to Python 2.x docs/Library Reference/Built-in Functions
BR2: open python.org
BR2: navigate to Python 3.x docs/Library Reference/Built-in Functions
BR1: find link to reload() function
BR2: find link to reload() function
BR1: link to reload() function should exist
BR2: link to reload() function should not exist"""
def test_1(firefox_browser3):
    def vishivanka_finder(firefox_browser3):
        ff = firefox_browser3.find_element_by_xpath('//input[@class = "input___3wRUz"]')
        sleep(1)
        return ff
    search_button = firefox_browser3.find_element_by_xpath('//input[@class = "input___3wRUz"]')#.send_keys('вишиванка')
    sleep(3)
    search_button.send_keys('вишиванка')
    search_button.send_keys(Keys.ENTER)
    sleep(10)
    search_results = firefox_browser3.find_elements_by_xpath('//div[@class = "cell___3mYuq"]')
    sleep(3)

    check.greater(len(search_results),0, 'Хоть что-то найдено')

    # sleep(3)
    dd = f'количество найденных элементов = {len(search_results)}'
    search_button = firefox_browser3.find_element_by_xpath('//input[@class = "input___3wRUz"]')

    sleep(3)
    search_button.clear()

    sleep(3)
    search_button.send_keys(dd)
    #в div-е два тега span. на нужный нам с ценой выходим через сиблинг с классом
    price_lst = firefox_browser3.find_elements_by_xpath('//div[@class = "price___9GCnp"]/span[@class = "hidden___6wtOd"]/following-sibling::span')
    #вытягиваем из веб-элемента атрибут text (то, что между тегами), убираем в конце валюту, убираем в середине пробелы и преобразуем в int,
    #суммируем все элементы массива и делим на количество элементов
    averaged_vishivanka_price = sum([int(price_lst[i].text[:-2].replace(' ', '')) for i in range(len(price_lst))])/len(price_lst)
    check.less(averaged_vishivanka_price,2500, 'Средняя цена на вышиванку должна быть меньше 2500грн')
    search_button.send_keys(f'averaged_vishivanka_price = {averaged_vishivanka_price}')

def test_4(firefox_browser4):
    register_button = firefox_browser4.find_element_by_xpath('//div[@class = "header__nav-button"]')
    register_button.click()
    check_box = firefox_browser4.find_element_by_xpath('//label[@class = "terms"]')
    check_box.click()
    inp_name = firefox_browser4.find_element_by_xpath('//input[@formcontrolname = "first_name"]')
    name_index = str(randint(100000,900000))
    inp_name.send_keys(name_index)
    inp_family = firefox_browser4.find_element_by_xpath('//input[@formcontrolname = "last_name"]')
    inp_family.send_keys('Мармонт')
    inp_email = firefox_browser4.find_element_by_xpath('//input[@formcontrolname = "email"]')

    print(name_index)
    inp_email.send_keys('marmont'+name_index+'@igra.pre')
    inp_passw = firefox_browser4.find_element_by_xpath('//input[@formcontrolname = "password"]')
    inp_passw.send_keys('derparol')

    submit_btt = firefox_browser4.find_element_by_xpath('//button[contains(@class,"login__form-btn")]')
    # inp_name.clear()
    # inp_name.send_keys(submit_btt.is_enabled())
    submit_btt.click()
    #проверка книпок на видимость(доступность проверится автоматом)
    # diprell
    assert logo_diprella_visibility(firefox_browser4), 'ссылка diprella видимая'
    # biblioteka
    # pochuk
    # lector
    # иконка учетки
    # лого посредине, фио под лого
    # головне
    # вподобання
    # налаштування курсив
    # профайл
    #
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC




    try:
        logo_link = firefox_browser4.find_element_by_xpath('//div[@class = "header__logo"]')
        assert logo_link.is_displayed(), 'Лого отображается'
    except exceptions.NoSuchElementException:
        assert False, 'вебэлемент //div[@class = "header__logo1"] отсутствует на странице'

    wait = WebDriverWait(firefox_browser4,5)
    try:
        library_dropdown = wait.until(EC.visibility_of((By.XPATH, '//div[@class = "library"]')))
        #signup_button = wait.until(C.element_to_be_clickable((By.CSS_SELECTOR, "a[href$=sign-up]")))
        #assert library_dropdown.is_displayed(), 'Лого отображается'
    except exceptions.NoSuchElementException:
        assert False, 'вебэлемент //div[@class = "library" отсутствует на странице'



def test_dropdownselect(firefox_browser4):
    from selenium.webdriver.support.select import Select
    dropdmenu = Select(firefox_browser4.find_elements_by_xpath('//div[contains(@class, "ui-dropdown-trigger")]'))
    dropdmenu.select_by_value('English')



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC








    # firefox_browser.fullscreen_window()
    # sleep(5)
    # firefox_browser.minimize_window()
    # sleep(5)
    # firefox_browser.maximize_window()
    # sleep(5)
    # firefox_browser.set_window_size(500, 200)
    # sleep(5)
    # firefox_browser.quit()
def test():
    firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
    firefox_capabilities['devtools.selfxss.count'] = 100
    firefox_capabilities['devtools.chrome.enabled'] = True
    firefox_capabilities['velikinax'] = True
    firefox_browserx = Firefox(executable_path=GeckoDriverManager().install(), desired_capabilities=firefox_capabilities)
    firefox_browserx.implicitly_wait(10)
    firefox_browserx.get('https://demo.diprella.com')
    firefox_browserx.maximize_window()


if __name__ == '__main__':
    pass

    # driver = webdriver.Remote()
    # driver.get('http://automationpractice.com/')
