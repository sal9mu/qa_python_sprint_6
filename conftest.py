import pytest
from selenium import webdriver
from test_data.data import TestData

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(TestData.url)
    driver.maximize_window()
    yield driver
    driver.quit()
