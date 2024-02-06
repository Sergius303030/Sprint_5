from conftest import *
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import Data as data

base_url = 'https://stellarburgers.nomoreparties.site/'

class TestLogin:
    def test_login_form_main_true(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.LOGIN_TITLE))
        driver.find_element(*Locators.FILD_EMAIL).send_keys(data.data_login)
        driver.find_element(*Locators.FILD_PASSWORD).send_keys(data.data_password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.MAIN_TITLE))
        assert driver.find_element(*Locators.BUTTON_CHECKOUT).text == 'Оформить заказ'

    def test_login_form_profile_true(self, driver):
        driver.find_element(*Locators.BUTTON_PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.LOGIN_TITLE))
        driver.find_element(*Locators.FILD_EMAIL).send_keys(data.data_login)
        driver.find_element(*Locators.FILD_PASSWORD).send_keys(data.data_password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.MAIN_TITLE))
        assert driver.find_element(*Locators.BUTTON_CHECKOUT).text == 'Оформить заказ'

    def test_login_form_registration_true(self, driver):
        driver.get(base_url + 'register')
        driver.find_element(*Locators.LINK_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.LOGIN_TITLE))
        driver.find_element(*Locators.FILD_EMAIL).send_keys(data.data_login)
        driver.find_element(*Locators.FILD_PASSWORD).send_keys(data.data_password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.MAIN_TITLE))
        assert driver.find_element(*Locators.BUTTON_CHECKOUT).text == 'Оформить заказ'

    def test_login_form_recovery_true(self, driver):
        driver.get(base_url + 'forgot-password')
        driver.find_element(*Locators.LINK_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.LOGIN_TITLE))
        driver.find_element(*Locators.FILD_EMAIL).send_keys(data.data_login)
        driver.find_element(*Locators.FILD_PASSWORD).send_keys(data.data_password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.MAIN_TITLE))
        assert driver.find_element(*Locators.BUTTON_CHECKOUT).text == 'Оформить заказ'