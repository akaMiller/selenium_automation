# Добавление товара в корзину через каталог

from selenium import webdriver
from selenium.webdriver.common.by import By
import auth_user

browser = webdriver.Chrome()


def test_add_products_from_catalog():
    auth_user.auth_user(browser)
    browser.find_element(By.CSS_SELECTOR,
                         ".inventory_item:first-of-type button[class='btn_primary btn_inventory']").click()
    browser.find_element(By.CSS_SELECTOR,
                         '.inventory_item:nth-child(2) button[class="btn_primary btn_inventory"]').click()
    # Можно добавить третий товар, чтобы вызвать ошибку
    # browser.find_element(By.CSS_SELECTOR,
    #                      '.inventory_item:nth-child(3) button[class="btn_primary btn_inventory"]').click()
    cart = browser.find_element(By.CSS_SELECTOR, "span[class='fa-layers-counter shopping_cart_badge']")
    assert cart.text == '2', 'В корзине не два товара!!!'
    browser.quit()
