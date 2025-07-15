import pytest
import allure
from conftest import driver
from page_objects.po_order_page import OrderPage
from utils.locators import Locators
from utils.data import TestData

class TestFlow:

    @allure.step('Проверка позитивного пользовательского сценария')
    @allure.description('Проверка позитивного сценария заказа от начала до конца')
    @pytest.mark.parametrize('button, person', [
        [Locators.high_button_order, TestData.person_1],
        [Locators.low_button_order, TestData.person_2]])
    def test_order_of_scooter_positive(self, driver, button, person):
        order_page = OrderPage(driver)
        order_page.accept_cookie()
        order_page.wait_visibility_of_element(button)
        order_page.scroll_to_element(button)
        order_page.click_on_element(button)
        order_page.first_form_of_order(person)
        order_page.second_form_of_order(person)
        assert order_page.check_element_is_displayed(Locators.button_status)