import pytest
from selenium import webdriver
from test_data.urls import TestURL

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(TestURL.url)
    driver.maximize_window()
    yield driver
    driver.quit()
