import pytest
from selenium import webdriver
from utils.urls import TestUrls


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(TestUrls.url_home_page)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()