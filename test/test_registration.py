from conftest import *
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import Data as data
import random

base_url = 'https://stellarburgers.nomoreparties.site/'

class TestRegistration:
    def test_registration_true(self, driver):
        driver.get(base_url + 'register')
        driver.find_element(*Locators.FILD_NAME).send_keys(data.data_name)
        driver.find_element(*Locators.FILD_EMAIL).send_keys(str(random.randint(10, 999)) + data.data_login)
        driver.find_element(*Locators.FILD_PASSWORD).send_keys(data.data_password)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.LOGIN_TITLE))
        assert driver.find_element(*Locators.LOGIN_TITLE).text == 'Вход'

    def test_registration_incorrect_password(self, driver):
        driver.get(base_url + 'register')
        driver.find_element(*Locators.FILD_NAME).send_keys(data.data_name)
        driver.find_element(*Locators.FILD_EMAIL).send_keys(str(random.randint(10, 999)) + data.data_login)
        driver.find_element(*Locators.FILD_PASSWORD).send_keys('123')
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        assert driver.find_element(*Locators.ERROR_MESSAGE).text == "Некорректный пароль"