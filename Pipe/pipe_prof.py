import os
import re
import time
import allure
from selenium.webdriver.common.by import By


@allure.epic("UI")
@allure.feature("Управление доступом")
class BasePage:
    @allure.title('Проверка ЛК')
    def aut(self):
