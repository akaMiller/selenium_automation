# Авторизация пользователя по логину и паролю

from selenium.webdriver.common.by import By

def auth_user(browser):
    browser.get('https://www.saucedemo.com/v1/')
    # Данные для авторизации доступны в коде, т.к. они открыто размещены на страницы входа :)
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
