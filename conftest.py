import pytest
from selenium import webdriver

base_url = 'https://stellarburgers.nomoreparties.site/'

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.get(base_url)
    yield driver
    driver.quit()