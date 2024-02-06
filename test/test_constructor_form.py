from conftest import *
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

base_url = 'https://stellarburgers.nomoreparties.site/'

class TestConstructorForm:
    def test_check_sauce(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.MAIN_TITLE))
        driver.find_element(*Locators.BUTTON_SAUCE).click()
        assert "tab_tab_type_current" in driver.find_element(*Locators.BUTTON_SAUCE).get_attribute('class')

    def test_check_filling(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.MAIN_TITLE))
        driver.find_element(*Locators.BUTTON_FILLING).click()
        assert "tab_tab_type_current" in driver.find_element(*Locators.BUTTON_FILLING).get_attribute('class')

    def test_check_ban(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.MAIN_TITLE))
        driver.find_element(*Locators.BUTTON_FILLING).click()
        driver.find_element(*Locators.BUTTON_BAN).click()
        assert "tab_tab_type_current" in driver.find_element(*Locators.BUTTON_BAN).get_attribute('class')