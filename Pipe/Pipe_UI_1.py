from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure

link = "https://brinex:12w13@dev-pipe.kolesa-darom.ru/service_versions"
browser: WebDriver = webdriver.Chrome()
browser.get(link)

class BasePage:
    def aut(self, aut, url):
        ioginaut = browser.find_element(By.XPATH, "//input[@type='email']")
        ioginaut.send_keys("Tests_Mikle@yandex.ru")
        passwordaut = browser.find_element(By.XPATH, "//input[@type='password']")
        passwordaut.send_keys('Tests_Mikle@yandex.ru')
        button_aut = browser.find_element(By.TAG_NAME, "button")
        button_aut.click()
        time.sleep(1)


"""Наличие заголовка страницы/Заголовков столбцов"""
elementH1 = browser.find_element(By.CLASS_NAME, "TheHeadTitle_head__title_H89gV")
heading1 = elementH1.text
assert "Версии сервисов" == heading1

# time.sleep(1)
element_H2 = browser.find_element(By.CLASS_NAME,'el-table_1_column_1.is-leaf.el-table__cell')
heading2 = element_H2.text
assert "Название сервиса" == heading2
# time.sleep(1)
element_H3 = browser.find_element(By.CLASS_NAME,'el-table_1_column_2.is-leaf.el-table__cell')
heading3 = element_H3.text
assert "Версия" == heading3
# time.sleep(1)
element_H4 = browser.find_element(By.CLASS_NAME,'el-table_1_column_3.is-leaf.el-table__cell')
heading4 = element_H4.text
assert "Дата создания" == heading4
# time.sleep(1)
element_H5 = browser.find_element(By.CLASS_NAME,'el-table_1_column_4.is-leaf.el-table__cell')
heading5 = element_H5.text
assert "Pipeline" == heading5
# time.sleep(1)
element_H6 = browser.find_element(By.CLASS_NAME,'el-table_1_column_5.is-leaf.el-table__cell')
heading6 = element_H6.text
assert "Tag" == heading6
# time.sleep(1)

"""Хлебные крошки/первый порядок"""
element_bc1 = browser.find_element(By.CLASS_NAME,'el-breadcrumb__inner.is-link')
bread_crumbs1 = element_bc1.text
assert "Главная страница" == bread_crumbs1
"""Хлебные крошки/второй порядок"""
element_bc2 = browser.find_element(By.XPATH,"//span[@class='el-breadcrumb__inner']")
bread_crumbs2 = element_bc2.text
assert "Версии сервисов" == bread_crumbs2

"""Подвал"""
bst1 = browser.find_element(By.CLASS_NAME,'TheFooter_about_hcOxy')
basement1 = bst1.text
assert "© 2022-2023 ООО «Колёса Даром». Все права защищены." == basement1
bst2 = browser.find_element(By.CLASS_NAME,'router-link-active.router-link-exact-active')
basement2 = bst2.text
assert "Версии сервисов" == basement2

#time.sleep(2)
browser.quit()

