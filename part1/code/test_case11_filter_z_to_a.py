# Проверка работоспособности фильтра (Z to A)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import auth_user

browser = webdriver.Chrome()


def test_filter_z_to_a():
    auth_user.auth_user(browser)
    # Сортируем по Z to A
    dropdown = Select(browser.find_element(By.CSS_SELECTOR, "select[class='product_sort_container']"))
    dropdown.select_by_value("za")
    # Получаем имена продуктов на странице
    products = browser.find_elements(By.CSS_SELECTOR, 'div.inventory_item_name')
    products_name = []
    for product in products:
        products_name.append(product.text)
    # Сравниваем с учетом сортировки
    assert products_name == sorted(products_name, reverse=True), 'Фильтр Z to A не работает!!!'
    browser.quit()
