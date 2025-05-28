import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from test_data.data import TestData



class OrderPage(BasePage):

    def open_page_order(self):
        self.wait_visibility_of_element(MainPageLocators.order_button_in_header)
        self.click_on_element(MainPageLocators.order_button_in_header)
        self.scroll_to_order_button(MainPageLocators.order_button_down_page)
        self.wait_visibility_of_order_button(MainPageLocators.order_button_down_page)
        self.click_on_element(MainPageLocators.order_button_down_page)

    @allure.step('Заполнение первой части формы и нажатие кнопки Далее')
    def filling_first_part_of_form(self, data):
        self.wait_visibility_of_element(OrderPageLocators.name)
        self.click_on_element(OrderPageLocators.name)
        self.send_keys_to_input(OrderPageLocators.name, data[0])
        self.click_on_element(OrderPageLocators.lastname)
        self.send_keys_to_input(OrderPageLocators.lastname, data[1])
        self.click_on_element(OrderPageLocators.address)
        self.send_keys_to_input(OrderPageLocators.address, data[2])
        self.click_on_element(OrderPageLocators.metro)
        self.send_keys_to_input(OrderPageLocators.metro, data[3])
        self.click_on_element(OrderPageLocators.select_dropdown_metro)
        self.click_on_element(OrderPageLocators.phone)
        self.send_keys_to_input(OrderPageLocators.phone, data[4])
        self.click_on_element(OrderPageLocators.button_next)

    @allure.step('Заполнение второй части формы и нажатие кнопки Заказать')
    def filling_second_part_of_form(self, data):
        self.wait_visibility_of_element(OrderPageLocators.date)
        self.click_on_element(OrderPageLocators.date)
        self.send_keys_to_input(OrderPageLocators.date, data[5])
        self.click_on_element(OrderPageLocators.calendar_item)
        self.wait_visibility_of_element(OrderPageLocators.rental_period)
        self.click_on_element(OrderPageLocators.rental_period)
        self.wait_visibility_of_element(OrderPageLocators.dropdown_rental_period)
        self.click_on_element(OrderPageLocators.dropdown_rental_period)
        self.click_on_element(OrderPageLocators.checkbox_grey_color)
        self.click_on_element(OrderPageLocators.comment)
        self.send_keys_to_input(OrderPageLocators.comment, data[6])
        self.click_on_element(OrderPageLocators.button_make_order)
        self.wait_visibility_of_element(OrderPageLocators.button_confirm_order)
        self.click_on_element(OrderPageLocators.button_confirm_order)
        self.wait_visibility_of_element(OrderPageLocators.title_successful_order)
        self.get_status_order()


    @allure.step('Выбор даты начала аренды из календаря')
    def click_date_in_calendar(self):
        self.click_on_element(OrderPageLocators.calendar_item)

    @allure.step('Отображение надписи о создании заказа')
    def get_status_order(self):
        return self.get_text_of_element(OrderPageLocators.title_successful_order)

    @allure.step('Проверка появления надписи об успешном создании заказа')
    def get_confirmation_text(self):
        try:
            return self.wait_visibility_of_element(
                OrderPageLocators.title_successful_order,
                timeout=5
            ).text
        except:
            return "Элемент подтверждения не найден"