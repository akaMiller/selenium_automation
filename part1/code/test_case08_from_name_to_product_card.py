# Кейс 8: Успешный переход к карточке товара после клика на название товара

from selenium import webdriver
from selenium.webdriver.common.by import By
import auth_user

browser = webdriver.Chrome()


def test_from_name_to_product_card():
    auth_user.auth_user(browser)
    # Можем получить ссылку на карточку продукта, чтобы потом ее сравнить с адресом продукта
    elem = browser.find_element(By.CSS_SELECTOR,
                                '.inventory_item:first-of-type .inventory_item_label [href]').get_attribute('href')
    # Ищем имя продукта и кликаем по нему
    browser.find_element(By.CSS_SELECTOR,
                         '.inventory_item:first-of-type .inventory_item_name:first-of-type').click()
    # Можем проверить, что карточка продукта совпадает с ссылкой в продукте
    assert browser.current_url == elem, 'Адрес страницы продукта не совпадает с выбранным продуктом!!!'
    # Проверяем, что перешли на новую страницу
    assert browser.current_url != 'https://www.saucedemo.com/v1/inventory.html', 'URL не соотвествует ожидаемому'
    browser.quit()
