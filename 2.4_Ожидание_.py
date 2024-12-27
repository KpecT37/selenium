import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")
'''Явное ожидание'''
# time.sleep(2)

'''Не явное ожидание'''
browser.implicitly_wait(5) # говорим WebDriver искать каждый элемент в течение 5 секунд
button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text