import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from lesson27.core.test_date.test_date import TestData


@pytest.fixture(scope="class")
def web_driver():
    driver: WebDriver=webdriver.Chrome()

    driver.maximize_window()
    driver.get(TestData.BASE_URL)

    yield driver

    driver.quit()

