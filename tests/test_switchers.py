import pytest
import allure
from conftest import driver
from page_objects.po_home_page import HomePage
from utils.locators import Locators
from utils.urls import TestUrls

class TestSwitchers:
    @allure.title('Переход на главную страницу по клику лого "Самокат"')
    @allure.description('Проверка, что при клике на лого "Самокат" из формы заказа происходит переход на главную страницу сайта')
    def test_logo_scooter_redirect_main_page(self, driver):
        home_page = HomePage(driver)
        home_page.wait_visibility_of_element(Locators.high_button_order)
        home_page.click_on_element(Locators.high_button_order)
        home_page.wait_visibility_of_element(Locators.field_name)
        home_page.wait_visibility_of_element(Locators.logo_scooter)
        home_page.click_on_element(Locators.logo_scooter)
        assert home_page.get_current_url() == TestUrls.url_home_page

    @allure.title('Переход на главную страницу Дзена при клике лого "Яндекс"')
    @allure.description('"Проверка, что при клике на лого "Яндекс" в шапке страницы происходит переход на главную страницу Дзена')
    def test_logo_yandex_redirect_dzen(self, driver):
        home_page = HomePage(driver)
        home_page.wait_visibility_of_element(Locators.high_button_order)
        home_page.click_on_element(Locators.high_button_order)
        home_page.wait_visibility_of_element(Locators.field_name)
        home_page.wait_visibility_of_element(Locators.logo_yandex)
        home_page.click_on_element(Locators.logo_yandex)
        home_page.switch_tab()
        home_page.wait_visibility_of_element(Locators.logo_dzen)
        assert home_page.get_current_url() == TestUrls.url_dzen