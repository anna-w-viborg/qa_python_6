import allure
import pytest
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Принять куки')
    def accept_cookie(self):
        self.driver.find_element(*Locators.cookie_button).click()

    @allure.step('Скроллим до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Ждем, когда элемент будет видно')
    def wait_visibility_of_element(self, locator):
        self.driver.find_element(locator)
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Кликаем на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Заполнить поле данными')
    def send_keys_to_field(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Получить текст элемента')
    def get_text_of_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Переключиться на другое окно')
    def switch_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получить заголовок страницы')
    def get_page_title(self, title_of_page):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(title_of_page))
        return self.driver.title

    @allure.step('Проверить, что элемент точно отображается')
    def check_element_is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()


