import os
import time

import pytest
from assertpy import assert_that
from dotenv import load_dotenv
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from lesson26.conftest import web_driver_creation


load_dotenv("keys_for_frames.env")
p_key1 = os.getenv('P_KEY1')
p_key2 = os.getenv('P_KEY2')
n_key1 = os.getenv('N_KEY1')
n_key2 = os.getenv('N_KEY2')


class TestInitialUiAutomation:
    BASE_URL: str = "http://localhost:8000/dz.html"

    def test_positive_authorization_frame_1(self, web_driver_creation):
        web_driver_creation.get(self.BASE_URL)
        web_driver_creation.switch_to.frame("frame1")
        secret_phrase_input_field: WebElement = web_driver_creation.find_element(By.XPATH, ".//*[@id='input1']")
        secret_phrase_input_field.click()
        secret_phrase_input_field.send_keys(p_key1)
        time.sleep(2)
        checking_button: WebElement = web_driver_creation.find_element(By.XPATH, ".//button[contains(@onclick, 'input1')]")
        checking_button.click()
        time.sleep(2)
        alert1 = Alert(web_driver_creation)
        assert_that (alert1.text).is_equal_to("Верифікація пройшла успішно!")
        print (f"\nTest: positive test of frame1 is passed - '{alert1.text}")
        alert1.accept()


    def test_positive_authorization_frame_2(self, web_driver_creation):
        web_driver_creation.get(self.BASE_URL)
        web_driver_creation.switch_to.frame("frame2")
        secret_phrase_input_field: WebElement = web_driver_creation.find_element(By.XPATH, ".//*[@id='input2']")
        secret_phrase_input_field.click()
        secret_phrase_input_field.send_keys(p_key2)
        time.sleep(2)
        checking_button: WebElement = web_driver_creation.find_element(By.XPATH, ".//button[contains(@onclick, 'input2')]")
        checking_button.click()
        time.sleep(2)
        alert2 = Alert(web_driver_creation)
        assert_that (alert2.text).is_equal_to("Верифікація пройшла успішно!")
        print (f"\nTest: positive test of frame2 is passed - '{alert2.text}")
        alert2.accept()

    def test_negative_authorization_frame_1(self, web_driver_creation):
        web_driver_creation.get(self.BASE_URL)
        web_driver_creation.switch_to.frame("frame1")
        secret_phrase_input_field: WebElement = web_driver_creation.find_element(By.XPATH, ".//*[@id='input1']")
        secret_phrase_input_field.click()
        secret_phrase_input_field.send_keys(n_key1)
        time.sleep(2)
        checking_button: WebElement = web_driver_creation.find_element(By.XPATH, ".//button[contains(@onclick, 'input1')]")
        checking_button.click()
        time.sleep(2)
        alert1 = Alert(web_driver_creation)
        assert_that (alert1.text).is_equal_to("Введено неправильний текст!")
        print (f"\nTest: negative test of frame1 is passed - '{alert1.text}")
        alert1.accept()

    def test_negative_authorization_frame_2(self, web_driver_creation):
        web_driver_creation.get(self.BASE_URL)
        web_driver_creation.switch_to.frame("frame2")
        secret_phrase_input_field: WebElement = web_driver_creation.find_element(By.XPATH, ".//*[@id='input2']")
        secret_phrase_input_field.click()
        secret_phrase_input_field.send_keys(n_key2)
        time.sleep(2)
        checking_button: WebElement = web_driver_creation.find_element(By.XPATH, ".//button[contains(@onclick, 'input2')]")
        checking_button.click()
        WebDriverWait(web_driver_creation, 10).until(EC.alert_is_present())   #Варіант заміни таймсліпу: діє таймсліп до поки не з'явиться алерт
        alert2 = Alert(web_driver_creation)
        assert_that (alert2.text).is_equal_to("Введено неправильний текст!")
        print (f"\nTest: negative test of frame2 is passed - '{alert2.text}")
        alert2.accept()





