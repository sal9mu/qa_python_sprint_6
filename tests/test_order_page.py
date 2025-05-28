import allure
import pytest
from conftest import driver
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from test_data.data import TestData
from pages.order_page import OrderPage
from pages.main_page import MainPage

class TestMakeAnOrder:

    @allure.title('Проверка успешного оформления заказа')
    @allure.description('Проверка успешного оформления заказа, с использованием двух разных точек '
                        'перехода на страницу заказа и двух разных наборов данных')
    @pytest.mark.parametrize('button, user_data', [
        (MainPageLocators.order_button_in_header, TestData.test_user_data1),
        (MainPageLocators.order_button_down_page, TestData.test_user_data2)
    ])

    def test_make_an_order(self, driver, button, user_data):
        with allure.step("Открытие формы заказа"):
            order_page = OrderPage(driver)
        with allure.step("Скролл до кнопки заказа внизу страницы"):
            order_page.scroll_to_element(button)
            order_page.wait_visibility_of_element(button)
            order_page.click_on_element(button)
        with allure.step("заполнение полей формы"):
            order_page.filling_first_part_of_form(user_data)
            order_page.filling_second_part_of_form(user_data)
        with allure.step("Проверка успешного оформления"):
            assert order_page.get_confirmation_text()
