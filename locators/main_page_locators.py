from selenium.webdriver.common.by import By


class MainPageLocators:
    order_button_in_header = (By.CLASS_NAME, "Button_Button__ra12g")
    order_button_down_page= (By.CLASS_NAME, "Home_FinishButton__1_cWm")
    home_header = (By.CLASS_NAME, "Home_Header__iJKdX")
    header_logo_scooter = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    header_logo_yandex = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    title_dzen = (By.XPATH, "//header[contains(@id, 'dzen-header')]")
    faq_section = (By.XPATH, '//div[contains(@class, "accordion")]')
    faq_questions = {
        1: [By.XPATH, '//div[@id="accordion__heading-0"]/parent::div'],
        2: [By.XPATH, '//div[@id="accordion__heading-1"]/parent::div'],
        3: [By.XPATH, '//div[@id="accordion__heading-2"]/parent::div'],
        4: [By.XPATH, '//div[@id="accordion__heading-3"]/parent::div'],
        5: [By.XPATH, '//div[@id="accordion__heading-4"]/parent::div'],
        6: [By.XPATH, '//div[@id="accordion__heading-5"]/parent::div'],
        7: [By.XPATH, '//div[@id="accordion__heading-6"]/parent::div'],
        8: [By.XPATH, '//div[@id="accordion__heading-7"]/parent::div']
    }
    faq_answers = {
        1: (By.XPATH, '//div[@id="accordion__panel-0"]'),
        2: (By.XPATH, '//div[@id="accordion__panel-1"]'),
        3: (By.XPATH, '//div[@id="accordion__panel-2"]'),
        4: (By.XPATH, '//div[@id="accordion__panel-3"]'),
        5: (By.XPATH, '//div[@id="accordion__panel-4"]'),
        6: (By.XPATH, '//div[@id="accordion__panel-5"]'),
        7: (By.XPATH, '//div[@id="accordion__panel-6"]'),
        8: (By.XPATH, '//div[@id="accordion__panel-7"]')
    }
