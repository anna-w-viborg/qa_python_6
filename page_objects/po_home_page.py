import pytest
import allure
import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.po_base_page import BasePage
from utils.locators import Locators

class HomePage(BasePage):


    #для тестирования вопросов
    @allure.step('Принять куки')
    def accept_cookie(self):
        self.driver.find_element(*Locators.cookie_button).click()

    @allure.step('Кликаем на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Проскроллить до раздела "Вопросы о важном"')
    def scroll_to_faq(self):
        self.scroll_to_element(Locators.faq_section)

    @allure.step('Ожидание видимости нужного вопроса')
    def wait_visibility_of_question(self, number: int):
        self.wait_visibility_of_element(Locators.button_q[number])

    @allure.step('Кликнуть на нужный вопрос "Вопросы о важном"')
    def click_question(self, number):
        self.driver.find_element(*Locators.button_q[number]).click()

    @allure.step('Ожидание видимости нужного ответа')
    def wait_visibility_of_answer(self, number: int):
        self.wait_visibility_of_element(Locators.answers[number])


    @allure.step('Получить текст нужного ответа')
    def get_answer_text(self, number):
        return self.get_text_of_element(Locators.answers[number])

    #для тестирования пользовательского сценария



