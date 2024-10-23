import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lesson28.core.pages.main_page import MainPage
from lesson28.core.pages.authorized_page import AuthorizedPage



class TestSearchDeliveries:
    main_page: MainPage
    authorized_page: AuthorizedPage

    def test_search_delivery_status(self, web_driver):
        self.main_page = MainPage(web_driver)
        self.authorized_page = AuthorizedPage(web_driver)

        self.main_page.new_user_registration()

        WebDriverWait(web_driver, 15).until(
            EC.url_contains("/panel/garage")
        )

        try:
            registration_status = WebDriverWait(web_driver, 15).until(
                EC.visibility_of_element_located(self.authorized_page.check_authorization_by_logout))
            assert registration_status.is_displayed(),"The logout button could not be found. Registration failed."
            print("The logout button is displayed. Registration was successful.")

        except TimeoutException:
            pytest.fail("Error! The logout button was not found on the page within 15 seconds. Registration failed.")

