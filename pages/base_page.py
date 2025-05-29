import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Подождать появления элемента')
    def wait_visibility_of_element(self, locator, time=6):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    @allure.step('Нажать на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ввод данных в поле')
    def send_keys_to_input(self, locator, data):
        self.driver.find_element(*locator).send_keys(data)

    @allure.step('Получить текст элемента')
    def get_text_of_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Заголовок страницы')
    def get_page_title(self, time=5):
        WebDriverWait(self.driver, time).until(EC.presence_of_element_located(MainPageLocators.title_dzen))
        return self.driver.title

    @allure.step('Проверка отображения элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Переход на другую вкладку')
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
