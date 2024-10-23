from selenium.webdriver.ie.webdriver import WebDriver

from lesson28.core.web_elements.abstract_element import AbstractElement


class InputField(AbstractElement):

    def __init__(self, driver:WebDriver, locator: tuple[str, str]) -> None:
        super().__init__(driver, locator)

    def fill (self, text: str) -> None:
        self.wait_for_visible().send_keys(text)
