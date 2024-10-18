from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from lesson27.core.pages.abstract_page import AbstractPage



class SearchPage(AbstractPage):
    _driver: WebDriver

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def delivery_status(self) -> str:
        element = self._driver.find_element(By.XPATH, ".//div[@class='header__status-text']")
        return element.text

