import pytest
import allure
from page_objects.po_home_page import HomePage
from utils.data import TestData
from conftest import driver
from utils.locators import Locators



@allure.title('Раздел "Вопросы о важном"')
@allure.description('Проверка раскрытия ответов при клике на вопросы в разделе "Вопросы о важном"')
@pytest.mark.parametrize('number, e_answer', enumerate(TestData.e_answer))
def test_click_question_show_answer(driver, number:int, e_answer):
    #зайти на сайт
    home_page = HomePage(driver)
    #принять куки, чтобы не загораживало
    home_page.accept_cookie()
    #прокрутить до раздела с вопросами
    home_page.scroll_to_faq()
    #подождать загрузку вопроса
    home_page.wait_visibility_of_question(number)
    #кликнуть вопрос
    home_page.click_question(number)
    #подождать загрузку ответа
    home_page.wait_visibility_of_answer(number)
    #сравнить ответы
    assert home_page.get_answer_text(number) == e_answer