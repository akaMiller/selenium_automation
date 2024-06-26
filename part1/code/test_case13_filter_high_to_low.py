# Проверка работоспособности фильтра (High to Low)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import auth_user

browser = webdriver.Chrome()


def test_filter_high_to_low():
    auth_user.auth_user(browser)
    # Сортируем по High to Low
    dropdown = Select(browser.find_element(By.CSS_SELECTOR, "select[class='product_sort_container']"))
    dropdown.select_by_value("hilo")
    # Получаем имена продуктов на странице
    products = browser.find_elements(By.CSS_SELECTOR, 'div.inventory_item_price')
    products_price = []
    for product in products:
        products_price.append(float(product.text[1:]))
    # Сравниваем с учетом сортировки
    assert products_price == sorted(products_price, reverse=True), 'Фильтр High to Low не работает!!!'
    browser.quit()
