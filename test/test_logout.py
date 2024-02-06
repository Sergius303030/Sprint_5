from conftest import *
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

base_url = 'https://stellarburgers.nomoreparties.site/'

class TestLogout:
    def test_logout_true(self, login):
        driver = login
        driver.find_element(*Locators.BUTTON_PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.HINT_PROFILE))
        driver.find_element(*Locators.BUTTON_LOGOUT).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.LOGIN_TITLE))
        assert driver.find_element(*Locators.LOGIN_TITLE).text == 'Вход'