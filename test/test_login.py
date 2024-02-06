from conftest import *
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

base_url = 'https://stellarburgers.nomoreparties.site/'

class TestLogin:
    def test_login_form_main_true(self, driver):
        driver.get(base_url)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.LOGIN_TITLE))
        driver.find_element(*Locators.FILD_EMAIL).send_keys('komarov_5@gmail.com')
        driver.find_element(*Locators.FILD_PASSWORD).send_keys('123456789')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.MAIN_TITLE))
        assert driver.find_element(*Locators.BUTTON_CHECKOUT).text == 'Оформить заказ'

    def test_login_form_profile_true(self, driver):
        driver.get(base_url)
        driver.find_element(*Locators.BUTTON_PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.LOGIN_TITLE))
        driver.find_element(*Locators.FILD_EMAIL).send_keys('komarov_5@gmail.com')
        driver.find_element(*Locators.FILD_PASSWORD).send_keys('123456789')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.MAIN_TITLE))
        assert driver.find_element(*Locators.BUTTON_CHECKOUT).text == 'Оформить заказ'

    def test_login_form_registration_true(self, driver):
        driver.get(base_url + 'register')
        driver.find_element(*Locators.LINK_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.LOGIN_TITLE))
        driver.find_element(*Locators.FILD_EMAIL).send_keys('komarov_5@gmail.com')
        driver.find_element(*Locators.FILD_PASSWORD).send_keys('123456789')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.MAIN_TITLE))
        assert driver.find_element(*Locators.BUTTON_CHECKOUT).text == 'Оформить заказ'

    def test_login_form_recovery_true(self, driver):
        driver.get(base_url + 'forgot-password')
        driver.find_element(*Locators.LINK_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.LOGIN_TITLE))
        driver.find_element(*Locators.FILD_EMAIL).send_keys('komarov_5@gmail.com')
        driver.find_element(*Locators.FILD_PASSWORD).send_keys('123456789')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.MAIN_TITLE))
        assert driver.find_element(*Locators.BUTTON_CHECKOUT).text == 'Оформить заказ'