import time

from pages.element_page import TextBoxPage
from pages.base_page import BasePage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test(driver):
    page = BasePage(driver, "https://www.google.com")
    page.open()
    time.sleep(5)


class TestElement:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_per_adder = text_box_page.check_filled_from()
            assert full_name == output_name
            assert email == output_email
            assert output_current_address == output_current_address
            assert permanent_address == output_per_adder
            print(output_name)
            print(output_email)
            print(output_current_address)
            print(output_per_adder)
