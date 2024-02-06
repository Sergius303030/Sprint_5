import pytest
from selenium import webdriver
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import Data as data

base_url = 'https://stellarburgers.nomoreparties.site/'

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.get(base_url)
    yield driver
    driver.quit()

@pytest.fixture()
def login(driver):
    driver.find_element(*Locators.BUTTON_LOGIN).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.LOGIN_TITLE))
    driver.find_element(*Locators.FILD_EMAIL).send_keys(data.data_login)
    driver.find_element(*Locators.FILD_PASSWORD).send_keys(data.data_password)
    driver.find_element(*Locators.BUTTON_LOGIN).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.MAIN_TITLE))
    return driver