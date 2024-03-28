# Кейс 7: Успешный переход к карточке товара после клика на картинку товара

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import auth_user


browser = webdriver.Chrome()


def test_from_picture_to_product_card():
    auth_user.auth_user(browser)
    # Можем получить ссылку из имени на карточку продукта, чтобы потом ее сравнить с адресом продукта
    elem = browser.find_element(By.CSS_SELECTOR,
                                '.inventory_item:first-of-type .inventory_item_label [href]').get_attribute('href')
    # Кликаем на картинку первого продукта
    browser.find_element(By.CSS_SELECTOR,
                         '.inventory_item:first-of-type div[class="inventory_item_img"]').click()
    # Можем проверить, что карточка продукта совпадает с ссылкой в продукте
    assert browser.current_url == elem, 'Адрес страницы продукта не совпадает с выбранным продуктом!!!'
    browser.quit()