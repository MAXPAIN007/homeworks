import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from assertpy import assert_that
from lesson27.core.pages.main_page import MainPage
from lesson27.core.pages.search_page import SearchPage
from selenium.webdriver.common.by import By


class TestSearchDeliveries:
    main_page: MainPage
    search_page: SearchPage

    @pytest.mark.parametrize("tracking_number, expected_status", [
        (20451020310311, "Отримана")])

    def test_search_delivery_status(self, web_driver, tracking_number,expected_status):
        self.main_page = MainPage(web_driver)
        self.search_page = SearchPage(web_driver)

        self.main_page.search_delivery(tracking_number)

        self.main_page.search_button.click()

        WebDriverWait(web_driver, 10).until(
            EC.url_contains("/chat/messages")
        )

        status_element = WebDriverWait(web_driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//div[@class='header__status-text']"))
        )

        assert_that(status_element.text).is_equal_to(expected_status)
        print(f"Статус посилки: {status_element.text}")

