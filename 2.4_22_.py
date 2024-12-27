from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

battonn = browser.find_element(By.ID, "book")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

battonn.click()

def calc(x):
     return str(math.log(abs(12*math.sin(int(x)))))
x = browser.find_element(By.ID, "input_value").text
y = calc(x)

imput = browser.find_element(By.CLASS_NAME, "form-control")
imput.send_keys(y)

Submit = browser.find_element(By.ID, "solve").click()

time.sleep(10)
browser.quit()


'''говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной'''
# button = WebDriverWait(browser, 5).until_not(EC.element_to_be_clickable((By.ID, "verify")))