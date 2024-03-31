# Выход из системы

from selenium import webdriver
from selenium.webdriver.common.by import By
import auth_user

browser = webdriver.Chrome()


def test_logout():
    auth_user.auth_user(browser)
    # Вызываем меню в левой верхнем углу
    browser.find_element(By.CSS_SELECTOR, '.bm-burger-button').click()
    # Ждем
    browser.implicitly_wait(0.5)
    # Кликаем на кнопку Logout
    browser.find_element(By.CSS_SELECTOR, '#logout_sidebar_link').click()
    # Сравниваем страницу
    assert browser.current_url == 'https://www.saucedemo.com/v1/index.html', 'URL не соотвествует ожидаемому'
    browser.quit()
