#Проверка работоспособности кнопки "Reset App State" в меню

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest
import auth_user

browser = webdriver.Chrome()


def test_check_about_button():
    auth_user.auth_user(browser)
    #Добавляем товар в корзину
    browser.find_element(By.CSS_SELECTOR,
                         ".inventory_item:first-of-type button[class='btn_primary btn_inventory']").click()
    #Проверяем что товар есть в корзине
    cart = browser.find_element(By.CSS_SELECTOR, "span[class='fa-layers-counter shopping_cart_badge']")
    assert cart.text == '1', 'В корзине не 1 товар!!!'
    #Вызываем меню в левой верхнем углу
    browser.find_element(By.CSS_SELECTOR, '.bm-burger-button').click()
    #Ждем
    browser.implicitly_wait(0.5)
    #Кликаем на кнопку Reset App State
    browser.find_element(By.CSS_SELECTOR, '#reset_sidebar_link').click()
    # Проверяем, что корзина пустая
    assert 'fa-layers-counter shopping_cart_badge' not in browser.page_source
    browser.quit()