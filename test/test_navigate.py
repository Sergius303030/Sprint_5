from conftest import *
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

base_url = 'https://stellarburgers.nomoreparties.site/'

class TestNavigate:
    def test_link_personal_account(self, login):
        driver = login
        driver.find_element(*Locators.BUTTON_PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.HINT_PROFILE))
        assert driver.current_url == base_url + 'account/profile'

    def test_link_constructor(self, login):
        driver = login
        driver.find_element(*Locators.BUTTON_PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.HINT_PROFILE))
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.MAIN_TITLE))
        assert driver.current_url == base_url

    def test_link_logo(self, login):
        driver = login
        driver.find_element(*Locators.BUTTON_PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.HINT_PROFILE))
        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.MAIN_TITLE))
        assert driver.current_url == base_url