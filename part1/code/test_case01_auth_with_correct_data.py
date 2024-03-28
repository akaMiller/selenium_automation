## Авторизация используя корректные данные

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import auth_user

browser = webdriver.Chrome()


def test_auth_positive():
    auth_user.auth_user(browser)
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory.html', 'URL не соотвествует ожидаемому'
    browser.quit()
