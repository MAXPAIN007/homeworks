from abc import ABC

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AbstractElement(ABC):
    _wrapped_element: WebElement

    def __init__(self, driver: WebDriver, locator: tuple[str, str]) -> None:
        self._driver = driver
        self._wrapped_element = self.find_element(locator)

    def find_element(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
        return WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_elements(self, locator: tuple[str, str], timeout: int = 10) -> list[WebElement]:
        return WebDriverWait(self._driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def wait_for_visible(self, timeout: int = 5) -> WebElement:
        return WebDriverWait(self._driver, timeout).until(
            EC.visibility_of(self._wrapped_element)
        )

    def wait_to_be_clickable(self, timeout: int = 5) -> WebElement:
        return WebDriverWait(self._driver, timeout).until(
            EC.element_to_be_clickable(self._wrapped_element)
        )
