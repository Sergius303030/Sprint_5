from conftest import *
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random

base_url = 'https://stellarburgers.nomoreparties.site/'

class TestRegistration:
    def test_registration_true(self, driver):
        new_name = f'komarov_5@gmail{random.randint(10, 999)}.com'
        driver.get(base_url + 'register')
        driver.find_element(*Locators.FILD_NAME).send_keys('Сергей')
        driver.find_element(*Locators.FILD_EMAIL).send_keys(new_name)
        driver.find_element(*Locators.FILD_PASSWORD).send_keys('123456789')
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.LOGIN_TITLE))
        assert driver.find_element(*Locators.LOGIN_TITLE).text == 'Вход'

    def test_registration_incorrect_password(self, driver):
        new_name = f'komarov_5@gmail{random.randint(10, 999)}.com'
        driver.get(base_url + 'register')
        driver.find_element(*Locators.FILD_NAME).send_keys('Сергей')
        driver.find_element(*Locators.FILD_EMAIL).send_keys(new_name)
        driver.find_element(*Locators.FILD_PASSWORD).send_keys('123')
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        assert driver.find_element(*Locators.ERROR_MESSAGE).text == "Некорректный пароль"