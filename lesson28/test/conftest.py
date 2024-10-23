import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from lesson28.core.test_data.test_data import TestData


@pytest.fixture(scope="class")
def web_driver():
    driver: WebDriver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(TestData.BASE_URL)

    yield driver

    driver.quit()

