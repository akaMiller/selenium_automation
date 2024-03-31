#Оформление заказа используя корректные данные

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import auth_user


browser = webdriver.Chrome()


def test_checkout_order():
    auth_user.auth_user(browser)
    #Можем получить ссылку на карточку продукта, чтобы потом ее сравнить с адресом продукта

    #Ищем имя продукта и кликаем по нему
    browser.find_element(By.CSS_SELECTOR,
                         '.inventory_item:first-of-type .inventory_item_name:first-of-type').click()
    #Кликаем на корзину
    browser.find_element(By.CSS_SELECTOR, '#shopping_cart_container').click()
    #Нажимаем кнопку Checkout в корзине
    browser.find_element(By.CSS_SELECTOR, "a[class='btn_action checkout_button']").click()
    #Вводим имя Adam в поле firstname
    browser.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Adam')
    #Вводим имя Smith в поле lastname
    browser.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Smith')
    #Вводим 10201 в поле zipcode
    browser.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('10201')
    #Нажимаем кнопку Contunie
    browser.find_element(By.CSS_SELECTOR, "input[class='btn_primary cart_button']").click()
    #Нажимаем кнопку finish
    browser.find_element(By.CSS_SELECTOR, "a[class='btn_action cart_button']").click()
    #Проверяем, что перешли на новую страницу
    assert browser.current_url == 'https://www.saucedemo.com/v1/checkout-complete.html', ('URL не соотвествует '
                                                                                          'ожидаемому')
    browser.quit()