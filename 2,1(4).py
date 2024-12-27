from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

try:
 browser: WebDriver = webdriver.Chrome()
 browser.get(link)


# time.sleep(2)
 input2 = browser.find_element(By.ID, "robotCheckbox")
 input2.click()
# time.sleep(2)
 input3 = browser.find_element(By.ID, "robotsRule")
 input3.click()
# time.sleep(2)
 input4 = browser.find_element(By.TAG_NAME, "button")
 input4.click()
# time.sleep(5)

finally:

   time.sleep(15) # успеваем скопировать код за 30 секунд
   browser.quit() # закрываем браузер после всех манипуляций
