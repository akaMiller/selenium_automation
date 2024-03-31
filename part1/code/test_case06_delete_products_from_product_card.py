# Удаляем продукт из карточки товара

from selenium import webdriver
from selenium.webdriver.common.by import By
import auth_user

browser = webdriver.Chrome()


def test_delete_product_from_product_card():
    auth_user.auth_user(browser)
    browser.find_element(By.CSS_SELECTOR,
                         '.inventory_item:first-of-type .inventory_item_name:first-of-type').click()
    browser.find_element(By.CSS_SELECTOR, "button[class='btn_primary btn_inventory']").click()
    browser.find_element(By.CSS_SELECTOR, "button[class='btn_secondary btn_inventory']").click()
    assert 'fa-layers-counter shopping_cart_badge' not in browser.page_source
    browser.quit()