import os
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from lesson28.core.web_elements.input_field import InputField
from lesson28.core.pages.abstract_page import AbstractPage
from lesson28.core.web_elements.button import Button
from dotenv import load_dotenv

load_dotenv("C:\\Users\\007\\PycharmProjects\\homeworks\\lesson28\\core\\test_data\\user_data.env")


class MainPage(AbstractPage):

    _driver:WebDriver

    def __init__(self, driver:WebDriver):
        super().__init__(driver)


    sing_up_button: Button = Button

    @property
    def sign_up_button(self) -> Button:
        return Button(self._driver, (By.XPATH, ".//button[contains(@class,'btn-primary') and contains(text(),'Sign up')]"))

    @property
    def registration_confirm_button(self) -> Button:
        return Button(self._driver, (By.XPATH, ".//button[contains(@class,'btn-primary') and contains(text(),'Register')]"))

    @property
    def first_name_field (self) -> InputField:
        return InputField(self._driver, (By.XPATH, ".//input[@id='signupName']"))

    @property
    def second_name_field (self) -> InputField:
        return InputField(self._driver, (By.XPATH, ".//input[@id='signupLastName']"))

    @property
    def email_field (self) -> InputField:
        return InputField(self._driver, (By.XPATH, ".//input[@id='signupEmail']"))

    @property
    def password_field (self) -> InputField:
        return InputField(self._driver, (By.XPATH, ".//input[@id='signupPassword']"))

    @property
    def duplicate_password_field (self) -> InputField:
        return InputField(self._driver, (By.XPATH, ".//input[@id='signupRepeatPassword']"))



    def new_user_registration (self):
        FIRST_NAME = os.getenv("FIRST_NAME")
        LAST_NAME = os.getenv("LAST_NAME")
        EMAIL = os.getenv("EMAIL")
        PASSWORD = os.getenv("PASSWORD")

        self.sign_up_button.click()
        self.first_name_field.fill(FIRST_NAME)
        self.second_name_field.fill(LAST_NAME)
        self.email_field.fill(EMAIL)
        self.password_field.fill(PASSWORD)
        self.duplicate_password_field.fill(PASSWORD)
        self.registration_confirm_button.click()


