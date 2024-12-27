from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
import os
import math

link = "http://suninjuly.github.io/file_input.html"

try:
    browser: WebDriver = webdriver.Chrome()
    browser.get(link)

    First_name = browser.find_element(By.NAME, "firstname")
    First_name.send_keys('jonny')
    Last_name = browser.find_element(By.NAME, "lastname")
    Last_name.send_keys('Smit')
    Email = browser.find_element(By.NAME, "email")
    Email.send_keys('JSmit@yyy.ry')

    file = browser.find_element(By.ID, "file")
    file_path = os.path.abspath(os.path.dirname("C:/Users/166/Desktop/Pyt/Pyt/poosto.txt"))
    file_name = os.path.join(file_path, 'poosto.txt')
    file.send_keys(file_name)

    Submit = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    Submit.click()
finally:
    time.sleep(10)
    browser.quit()
