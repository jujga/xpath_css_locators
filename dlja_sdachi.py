from time import sleep
import pytest_check as check
import pytest
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def firefox_browser3():
    # firefox_browser4 = Firefox()
    firefox_browser3 = Firefox(executable_path=GeckoDriverManager().install())
    firefox_browser3.get('https://www.joom.com/uk')

    yield firefox_browser3
    firefox_browser3.close()


def test_1(firefox_browser3):
    def search_vishivanka():
        search_button = firefox_browser3.find_element_by_xpath(
            '//input[@class = "input___3wRUz"]')  # .send_keys('вишиванка')
        sleep(1)
        search_button.send_keys('вишиванка')
        search_button.send_keys(Keys.ENTER)
        sleep(3)

    def averaged_vishivanka_price():
        # в div-е два тега span. на нужный нам с ценой выходим через сиблинг с классом
        price_lst = firefox_browser3.find_elements_by_xpath(
            '//div[@class = "price___9GCnp"]/span[@class = "hidden___6wtOd"]/following-sibling::span')
        # вытягиваем из веб-элемента атрибут text (то, что между тегами), убираем в конце валюту, убираем в середине пробелы и преобразуем в int,
        # суммируем все элементы массива и делим на количество элементов
        return round(sum([int(price_lst[i].text[:-2].replace(' ', '')) for i in range(len(price_lst))]) / len(price_lst), 0)

    search_vishivanka()  # ищем вышиванку
    search_results = firefox_browser3.find_elements_by_xpath('//div[@class = "cell___3mYuq"]')
    sleep(1)

    assert search_results, 'Хоть что-то найдено'
    assert averaged_vishivanka_price() < 2500, 'Средняя цена на вышиванку должна быть меньше 2500грн'
