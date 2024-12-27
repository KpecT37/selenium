from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, "//div[@class='form-group first_class']//input[@required]")
    input1.send_keys("Ivan")
    time.sleep(1)
    input2 = browser.find_element(By.XPATH, "//div[@class='form-group second_class']//input[@required]")
    input2.send_keys("Petrov")
    time.sleep(1)
    input3 = browser.find_element(By.XPATH, "//div[@class='form-group third_class']//input[@required]")
    input3.send_keys("eMail")
    time.sleep(1)
   # input4 = browser.find_element(By.ID, "country")
   # input4.send_keys("Russia")
   # time.sleep(5)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()