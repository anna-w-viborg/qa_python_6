import allure
from utils.locators import Locators
from page_objects.po_base_page import BasePage
from utils.data import TestData

class OrderPage(BasePage):

    @allure.step('Заполнить форму "Для кого самокат"')
    def first_form_of_order(self, person):
        #подождать прогрузки поля "Имя"
        self.wait_visibility_of_element(Locators.field_name)
        #кликнуть на поле "Имя"
        self.click_on_element(Locators.field_name)
        #вставить данные в поле "Имя"
        self.send_keys_to_field(Locators.field_name, person[0])
        #кликнуть на поле "Фамилия"
        self.click_on_element(Locators.field_lastname)
        #вставить данные в поле "Фамилия"
        self.send_keys_to_field(Locators.field_lastname, person[1])
        #кликнуть на поле "Адрес"
        self.click_on_element(Locators.fiels_adress)
        #вставить данные в поле "Адрес"
        self.send_keys_to_field(Locators.fiels_adress, person[2])
        #кликнуть на поле "Станция метро"
        self.click_on_element(Locators.field_subway)
        #ввести станцию метро
        self.send_keys_to_field(Locators.field_subway, person[3])
        #выбрать станцию метро из выпадающего списка
        self.click_on_element(Locators.list_of_subway)
        #кликнуть на поле "Телефон"
        self.click_on_element(Locators.field_phone)
        #вставить данные в поле "Телефон"
        self.send_keys_to_field(Locators.field_phone, person[4])
        #кликнуть на кнопку "Далее"
        self.click_on_element(Locators.button_next)

    @allure.step('Заполнить форму "Про аренду"')
    def second_form_of_order(self, person):
        #подождать загрузки поля "Когда привезти самокат"
        self.wait_visibility_of_element(Locators.field_when)
        #кликнуть на поле "Когда привезти самокат"
        self.click_on_element(Locators.field_when)
        #вставить данные в поле "Когда привезти самокат"
        self.send_keys_to_field(Locators.field_when, person[5])
        #кликнуть на поле "Срок аренды"
        self.click_on_element(Locators.field_how_long)
        #кликнуть на срок "сутки"
        self.click_on_element(Locators.set_how_long)
        #кликнуть на черный чекбокс
        self.click_on_element(Locators.checkbox_color)
        #кликнуть на поле "Комментарий для курьера"
        self.click_on_element(Locators.field_comment)
        #вставить данные в поле "Комментарий для курьера"
        self.send_keys_to_field(Locators.field_comment, person[6])
        #кликнуть на кнопку "Заказать
        self.click_on_element(Locators.button_2f_last)
        #кликнуть на кнопку подтверждения заказа
        self.click_on_element(Locators.button_yes)
        #проверить, что заказ создан и появилась кнопка "Статус заказа"
        self.wait_visibility_of_element(Locators.button_status)