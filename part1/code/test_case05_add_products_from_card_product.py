## Добавление товара в корзину из карточки товара

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import auth_user


browser = webdriver.Chrome()


def test_add_product_from_card_product():
    auth_user.auth_user(browser)
    # Можем получить ссылку на карточку продукта, чтобы потом ее сравнить с адресом продукта
    # elem = browser.find_element(By.CSS_SELECTOR,
    #                             '.inventory_item:first-of-type .inventory_item_label [href]').get_attribute('href')
    browser.find_element(By.CSS_SELECTOR,
                         '.inventory_item:first-of-type .inventory_item_name:first-of-type').click()
    # Можем проверить, что карточка продукта совпадает с ссылкой в продукте
    # assert browser.current_url == elem , 'Адрес страницы продукта не совпадает с выбранным продуктом!!!'
    browser.find_element(By.CSS_SELECTOR, "button[class='btn_primary btn_inventory']").click()
    cart = browser.find_element(By.CSS_SELECTOR, "span[class='fa-layers-counter shopping_cart_badge']")
    assert cart.text == '1', 'В корзине не один товара!!!'
    browser.quit()

