
import pytest_check as check
import pytest
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from random import randint
from selenium import webdriver
from  selenium.common import exceptions
from fixtures import browser, Config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#helper function
def get_random_num_name():
    return str(randint(100000, 900000))


from diprella_locators_module import WebElements

def check_visibility(webelement):
    #проверка книпок на видимость(доступность проверится автоматом)
    # diprell
    try:
        assert webelement.get().is_displayed(), f'Вебэлемент {webelement}'
    except exceptions.NoSuchElementException:
        assert False, f'вебэлемент {webelement} отсутствует на странице'


    #использую проперти element_to_be_clickable, т.к. visibility_of почему-то бьет ошибку
def check_editable(strategy_locator):
    wait = WebDriverWait(Config.browser, 5)
    try:
        assert wait.until(EC.element_to_be_clickable(strategy_locator)), 'хрень кликабельна'
    except exceptions.NoSuchElementException:
        assert False, f'вебэлемент {strategy_locator[1]} отсутствует на странице'


def test_4():

    WebElements.REGISTER_BUTTON.get().click()
    WebElements.CHECK_BOX_I_HAVE_READ.get().click()
    name_index = get_random_num_name()
    WebElements.INP_NAME.get().send_keys(name_index)

    WebElements.INP_FAMILY.get().send_keys('Мармонт')

    WebElements.INP_EMAIL.get().send_keys('marmont'+name_index+'@igra.pre')
    WebElements.INP_PASSW.get().send_keys('derparol')
    WebElements.SUBMIT_BTT.get().click()

    #assert logo_diprella_visibility(Config.browser), 'ссылка diprella видимая'
    check_visibility(WebElements.LOGO_LINK)
    # biblioteka
    check_editable(WebElements.LIBRARY.strategy_locator)
    # профайл
    check_visibility(WebElements.PROFILE_LINK)

    # pochuk. редактируемость проверим путем записи в данный вебэлемента текста с последующим считыванием.
    # препод редактируемость рекомендовал проверять с помошью element_to_be_clickable, когда нибудь переделаю. может быть...
    try:
        pochuk = Config.browser.find_element_by_xpath('//input[@id = "search"]')
        pochuk.send_keys('some text')
        assert pochuk.get_attribute ("value") == 'some text'
        pochuk.clear() #чтобы не мешало читать остальное на сайте, очищаем поле
        Config.browser.find_element_by_xpath('//div[contains(@class, "close__search") and contains(@class, "ng-star-inserted")]').click()    #и жмем крестик

        pass
    except exceptions.NoSuchElementException: #если вебэлемент не найден, перехватываем соответствующее сообщение и
        # вываливаем псевдоассерт с псевдонесовпадением
        assert False, 'вебэлемент //input[@id = "search"] отсутствует на странице либо не доступен для редактирования'


    # lector
    # иконка учетки
    # лого посредине, фио под лого
    # головне
    # вподобання
    # налаштування курсив




if __name__ == '__main__':
    pass

