from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

 #Ссылка на страницу
link = "https://suninjuly.github.io/selects1.html"

try:
    # Инициализация браузера
    browser: WebDriver = webdriver.Chrome()
    browser.get(link)
    # Получаем значения чисел
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    # Считаем сумму
    sum_result = int(num1) + int(num2)
    # Выбираем сумму в выпадающем списке
    browser.find_element(By.CLASS_NAME, "custom-select").click()
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(sum_result))

    # Нажимаем кнопку "Submit"
    browser.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(10)

finally:
    # Закрываем браузер
    browser.quit()
