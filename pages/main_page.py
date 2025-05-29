import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from test_data.data import TestData


class MainPage(BasePage):

    @allure.step('Подождать появления кнопки "Заказать" в хедере')
    def wait_visibility_of_order_button_in_header(self):
        self.wait_visibility_of_element(MainPageLocators.order_button_in_header)

    @allure.step('Нажать кнопку "Заказать" в хедере')
    def click_on_order_button_in_header(self):
        self.click_on_element(MainPageLocators.order_button_in_header)

    @allure.step('Подождать появления лого "Самокат" в хедере')
    def wait_visibility_of_scooter_logo_in_header(self):
        self.wait_visibility_of_element(MainPageLocators.header_logo_scooter)

    @allure.step('Нажать на логотип "Самокат" в хедере')
    def click_on_scooter_in_header(self):
        self.click_on_element(MainPageLocators.header_logo_scooter)

    @allure.step('Подождать появления лого "Яндекс" в хедере')
    def wait_visibility_of_yandex_logo_in_header(self):
        self.wait_visibility_of_element(MainPageLocators.header_logo_yandex)

    @allure.step('Нажать на логотип "Яндекс" в хедере')
    def click_on_yandex_in_header(self):
        self.click_on_element(MainPageLocators.header_logo_yandex)

    @allure.step('Подождать появления заголовка главной страницы Дзена')
    def wait_logo_main_page_dzen(self):
        self.wait_visibility_of_element(MainPageLocators.title_dzen)

    @allure.step('Подождать появления заголовка главной страницы')
    def wait_logo_main_page(self):
        self.wait_visibility_of_element(MainPageLocators.home_header)

    @allure.step('Получение названия страницы "Дзен"')
    def get_page_dzen_title(self):
        return self.get_text_of_element(MainPageLocators.title_dzen)

    @allure.step('Проверить отображение заголовка главной страницы')
    def check_main_page_logo(self):
        return self.check_displaying_of_element(MainPageLocators.home_header)

    @allure.step('Скролл до кнопки Заказать')
    def scroll_to_order_button(self):
        self.scroll_to_element(MainPageLocators.order_button_down_page)

    @allure.step('Подождать появления кнопки Заказать')
    def wait_visibility_of_order_button(self):
        self.wait_visibility_of_element(MainPageLocators.order_button_down_page)

    @allure.step('Скролл до раздела с вопросами')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.faq_section)

    @allure.step('Подождать появления нужного номера вопроса')
    def wait_visibility_of_faq_question(self, question_id):
        self.wait_visibility_of_element(MainPageLocators.faq_questions[question_id])

    @allure.step('Нажать на нужный номер вопроса')
    def click_on_faq_question(self, question_id):
        self.click_on_element(MainPageLocators.faq_questions[question_id])

    @allure.step('Подождать появления нужного номера ответа на вопрос')
    def wait_visibility_of_faq_answer(self, answers_id):
        self.wait_visibility_of_element(MainPageLocators.faq_answers[answers_id])

    @allure.step('Получить текст нужного ответа')
    def get_text_from_faq_answer(self, answers_id):
        return self.get_text_of_element(MainPageLocators.faq_answers[answers_id])
