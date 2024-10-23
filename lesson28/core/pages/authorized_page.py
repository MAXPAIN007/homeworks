from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from lesson28.core.pages.abstract_page import AbstractPage



class AuthorizedPage(AbstractPage):
    _driver: WebDriver

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def check_authorization_by_logout(self):
        return By.XPATH, "//span[contains(@class, 'logout')]"


# https://guest:welcome2qauto@qauto2.forstudy.space/panel/garage