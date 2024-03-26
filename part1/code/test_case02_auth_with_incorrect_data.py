##Авторизация используя некорректные данные (user, user)

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


browser = webdriver.Chrome()

def test_auth_negative():

    browser.get('https://www.saucedemo.com/v1/')
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('user')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.find_element(By.CLASS_NAME, 'error-button'), 'Нет кнопки ошибки!!!'
    browser.quit()