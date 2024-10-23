from selenium.webdriver.ie.webdriver import WebDriver
from lesson28.core.web_elements.abstract_element import AbstractElement


class Button(AbstractElement):

    def __init__(self, driver: WebDriver, locator: tuple[str, str]):
        super().__init__(driver, locator)

    def click (self):
        self.wait_to_be_clickable().click()
