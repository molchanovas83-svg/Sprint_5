import random
from data import Data
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestCreateCard:
    def test_create_card_unauthorized_user(self, driver):
        driver.find_element(*Locators._CREATE_MESSAGE_BUTTON).click()  # Нажать кнопку "Разместить объявление"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators._ALERT))  # Авторизуйтесь

    def test_create_card_authorized_user(self, driver):
        driver.find_element(*Locators._ENTER_AND_REGISTRATION_BUTTON).click()  # Нажать кнопку "Вход и регистрация"
        driver.find_element(*Locators._EMAIL_INPUT).send_keys(Data.USER_EMAIL)  # Заполнить поле Email
        driver.find_element(*Locators._EMAIL_PASSWORD).send_keys(Data.USER_PASSWORD)  # Заполнить поле Password
        driver.find_element(*Locators._LOGIN_BUTTON).click()  # Нажать кнопку "Войти"
        # Проверить
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators._USER_AVATAR))  # Ожидание
        driver.find_element(*Locators._CREATE_MESSAGE_BUTTON).click()  # Нажать кнопку "Разместить объявление"
        name = f'Товар {random.randint(100, 999)}'
        driver.find_element(*Locators._NAME).send_keys(name)  # Заполнить "Название"
        driver.find_element(*Locators._DESCRIPTION).send_keys('Отличный товар!')  # Заполнить "Описание"
        driver.find_element(*Locators._PRICE).send_keys(500)  # Ввести "Стоимость"
        driver.find_element(*Locators._CATEGORY).click()  # Выбрать категорию
        driver.find_element(*Locators._PUBLISH_BUTTON).click()  # Нажать кнопку "Опубликовать"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators._USER_AVATAR)).click()
        assert driver.find_element(*Locators._ABOUT).text == name  # Созданное объявление отображается
