import pytest
import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lesson28.core.pages.main_page import MainPage
from lesson28.core.pages.authorized_page import AuthorizedPage


@allure.feature('User Registration')
class TestUserRegistration:
    main_page: MainPage
    authorized_page: AuthorizedPage

    @allure.story('Register new user and verify authorization')
    @allure.step("Test registration and check if the logout button is visible")
    def test_user_registered(self, web_driver):
        with allure.step("Initialize MainPage and AuthorizedPage objects"):
            self.main_page = MainPage(web_driver)
            self.authorized_page = AuthorizedPage(web_driver)

        with allure.step("Perform new user registration"):
            self.main_page.new_user_registration()

        with allure.step("Wait for the URL to contain '/panel/garage'"):
            WebDriverWait(web_driver, 15).until(
                EC.url_contains("/panel/garage")
            )

        with allure.step("Check if the logout button is displayed after registration"):
            try:
                registration_status = WebDriverWait(web_driver, 15).until(
                    EC.visibility_of_element_located(self.authorized_page.check_authorization_by_logout))

                assert registration_status.is_displayed(), "The logout button could not be found. Registration failed."
                allure.attach(body="The logout button is displayed. Registration was successful.",
                              name="SuccessMessage", attachment_type=allure.attachment_type.TEXT)

            except TimeoutException:
                allure.attach(
                    body="The logout button was not found on the page within 15 seconds. Registration failed.",
                    name="ErrorMessage", attachment_type=allure.attachment_type.TEXT)
                pytest.fail(
                    "Error! The logout button was not found on the page within 15 seconds. Registration failed.")
