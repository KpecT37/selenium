from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser: WebDriver = webdriver.Chrome()
    browser.get(link)
    BT_go = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    BT_go.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    def calc(summ):
     return str(math.log(abs(12*math.sin(int(summ)))))

    summ = browser.find_element(By.ID, "input_value").text
    y = calc(summ)
    input1 = browser.find_element(By.CLASS_NAME, "form-control")
    input1.send_keys(y)
    ss = browser.find_element(By.CLASS_NAME, "form-control")
    ss.send_keys(y)

    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()
finally:
   time.sleep(10)
   browser.quit()
