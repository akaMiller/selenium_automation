## Добавление товара в корзину через каталог

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


browser = webdriver.Chrome()

def test_add_products_from_catalog():

    browser.get('https://www.saucedemo.com/v1/')
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    browser.implicitly_wait(0.5)
    browser.find_element(By.CSS_SELECTOR, ".inventory_item:first-of-type button[class='btn_primary btn_inventory']").click()
    browser.find_element(By.CSS_SELECTOR,
                         '.inventory_item:nth-child(2) button[class="btn_primary btn_inventory"]').click()
    cart = browser.find_element(By.CSS_SELECTOR, "span[class='fa-layers-counter shopping_cart_badge']")
    assert cart.text == '2', 'В корзине не два товара!!!'
    browser.quit()