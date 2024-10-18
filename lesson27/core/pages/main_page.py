from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from lesson27.core.pages.abstract_page import AbstractPage
from lesson27.core.web_elements.button import Button
from lesson27.core.web_elements.input_field import InputField


class MainPage(AbstractPage):

    _driver:WebDriver

    def __init__(self, driver:WebDriver):
        super().__init__(driver)

    search_button: Button = Button

    @property
    def search_button(self) -> Button:
        return Button(self._driver, (By.XPATH, ".//input[@id='np-number-input-desktop-btn-search-en']"))

    @property
    def search_field_by_delivery_number (self) -> InputField:
        return InputField(self._driver, (By.XPATH, "//input[@id='en']"))

    @property
    def delivery_status(self) -> str:
        element = self._driver.find_element(By.XPATH, ".//div[@class='header__status-text']")
        return element.text

    def search_delivery (self, delivery_number:int):
        self.search_field_by_delivery_number.fill(delivery_number)

        self.search_button.click()

