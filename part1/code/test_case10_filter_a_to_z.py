#Проверка работоспособности фильтра (A to Z)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest
import auth_user


browser = webdriver.Chrome()
def test_filter_a_to_z():
    auth_user.auth_user(browser)
    #сортируем по A to Z
    dropdown = Select(browser.find_element(By.CSS_SELECTOR, "select[class='product_sort_container']"))
    dropdown.select_by_value("az")
    #Получаем имена продуктов на странице
    products = browser.find_elements(By.CSS_SELECTOR, 'div.inventory_item_name')
    products_name = []
    for product in products:
        products_name.append(product.text)
    #Сравниваем с учетом сортировки
    assert products_name == sorted(products_name, reverse=False), 'Фильтр A to Z не работает!!!'
    browser.quit()