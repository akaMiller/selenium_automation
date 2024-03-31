# Проверка работоспособности кнопки "About" в меню

from selenium import webdriver
from selenium.webdriver.common.by import By
import auth_user

browser = webdriver.Chrome()


def test_check_about_button():
    auth_user.auth_user(browser)
    # Вызываем меню в левой верхнем углу
    browser.find_element(By.CSS_SELECTOR, '.bm-burger-button').click()
    # Ждем
    browser.implicitly_wait(0.5)
    # Кликаем на кнопку About
    browser.find_element(By.CSS_SELECTOR, '#about_sidebar_link').click()
    # Сравниваем страницу
    assert browser.current_url == 'https://saucelabs.com/', 'URL не соотвествует ожидаемому'
    browser.quit()
