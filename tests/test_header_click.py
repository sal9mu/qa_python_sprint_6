import allure
import pytest
from conftest import driver
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from test_data.data import TestData



class TestHeader:
    @allure.description('Проверки переходов по клику на лого в хедере')
    @allure.title('Проверка перехода на главную страницу по кликуна лого "Самокат"')
    def test_logo_scooter_to_main_page(self, driver):
        with allure.step("Открытие главной страницы"):
            main_page = MainPage(driver)
        with allure.step("Ожидание появления кнопки Заказать и нажатие кнопки"):
            main_page.wait_visibility_of_order_button_in_header()
            main_page.click_on_order_button_in_header()
        with allure.step("Ожидание логотипа Самокат и нажатие на него"):
            main_page.wait_visibility_of_scooter_logo_in_header()
            main_page.click_on_scooter_in_header()
        with allure.step("Ожидание появления логотипа главной страницы"):
            main_page.wait_logo_main_page()
        with allure.step("Проверка наличия логотипа на главной странице"):
            assert main_page.check_main_page_logo()

    @allure.title('Проверка перехода на страницу "Дзена" по клику на лого "Яндекс" в хедере')
    def test_logo_yandex_to_dzen(self, driver):
        with allure.step("Открытие главной страницы"):
            main_page = MainPage(driver)
        with allure.step("Ожидание появления логотипа Яндекс и нажатие на него"):
            main_page.wait_visibility_of_yandex_logo_in_header()
            main_page.click_on_yandex_in_header()
        with allure.step("Переход на другую вкладку"):
            main_page.switch_to_new_window()
        with allure.step("Ожидание появления логотипа главной страницы Дзена"):
            main_page.wait_logo_main_page_dzen()
            main_page.get_page_dzen_title()
        with allure.step("Проверка наличия слова Дзен в url"):
            assert 'dzen' in TestData.dzen
