import allure
import pytest
from conftest import driver
from locators.main_page_locators import MainPageLocators
from test_data.data import TestData
from pages.main_page import MainPage



class TestMainPageFaq:
    @allure.title('Проверки блока с вопросами')
    @allure.description('Проверка соответствия текста в ответах на вопросы')
    @pytest.mark.parametrize('question_id, expected_answer', TestData.test_questions_answer_data)
    def test_check_faq_answer(self, driver, question_id, expected_answer):
        with allure.step("Открытие главной страницы"):
            main_page = MainPage(driver)
        with allure.step("Скролл до раздела с вопросами"):
            main_page.scroll_to_faq_section()
        with allure.step("Ожидание появления раздела с вопросами и нажатие на вопросы"):
            main_page.wait_visibility_of_faq_question(question_id)
            main_page.click_on_faq_question(question_id)
        with allure.step("Ожидание появления ответа на выбранный вопрос"):
            main_page.wait_visibility_of_faq_answer(question_id)
            actual_answer = main_page.get_text_from_faq_answer(question_id)
        with allure.step("Проверка соответствия текста ответа на выбранный вопрос"):
            assert actual_answer == expected_answer
