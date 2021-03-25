import pytest
from selenium import webdriver
from utils.constants import DEFAULT_WAIT_TIME


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(DEFAULT_WAIT_TIME)
    driver.maximize_window()

    yield driver
    driver.quit()
