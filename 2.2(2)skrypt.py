import math
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser: WebDriver = webdriver.Chrome()
    browser.get(link)
    def calc(x):
     return str(math.log(abs(12*math.sin(int(x)))))
    summ = browser.find_element(By.ID, "input_value").text
    y = calc(summ)
    input1 = browser.find_element(By.CLASS_NAME, "form-control")
    input1.send_keys(y)
    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click()
    input3 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input3)
    input3.click()


    button = browser.find_element(By.XPATH, "//button[normalize-space()='Submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    time.sleep(10)

finally:
    # Закрываем браузер
    browser.quit()
