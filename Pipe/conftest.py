# -*- coding: utf-8 -*-
import os
import time
import pytest
from selenium import webdriver
import requests
import allure
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import logging
from dotenv import load_dotenv
import configparser

load_dotenv()

link_UAT = "https://" + os.getenv("HTTP") + "kazan-uat.kolesa-darom.ru/"
link_EXTERNAL = "https://" + os.getenv("HTTP") + "external.kolesa-darom.ru/"
link_FEED1 = "https://" + os.getenv("HTTP") + "spb.kolesa-darom.ru/"
link_FEED1_2 = "https://" + os.getenv("HTTP") + "spb.kolesa-darom.ru/"
link_FEED2 = "https://" + os.getenv("HTTP") + "nn.kolesa-darom.ru/"
link_FEED2_2 = "https://" + os.getenv("HTTP") + "nn.kolesa-darom.ru/"
link_WEB_BOT1 = "https://miass.kolesa-darom.ru/"
link_WEB_BOT1_2 = "https://" + os.getenv("HTTP") + "miass.kolesa-darom.ru/"
link_WEB_BOT2 = "https://barnaul.kolesa-darom.ru/"
link_WEB_BOT2_2 = "https://" + os.getenv("HTTP") + "barnaul.kolesa-darom.ru/"
link_WEB4 = "https://perm.kolesa-darom.ru/"
link_WEB4_2 = "https://" + os.getenv("HTTP") + "perm.kolesa-darom.ru/"
link_WEB3 = "https://tver.kolesa-darom.ru/"
link_WEB3_2 = "https://" + os.getenv("HTTP") + "tver.kolesa-darom.ru/"
link_WEB2 = "https://saratov.kolesa-darom.ru/"
link_WEB2_2 = "https://" + os.getenv("HTTP") + "saratov.kolesa-darom.ru/"
link_WEB1 = "https://tambov.kolesa-darom.ru/"
link_WEB1_2 = "https://" + os.getenv("HTTP") + "tambov.kolesa-darom.ru/"
link_WEB = "https://www.kolesa-darom.ru/"
link_CDN_UAT = "https://cdn-uat.kolesa-darom.ru/"
link_CDN_EXTERNAL = "https://cdn-external.kolesa-darom.ru/"
link_CDN_1 = "https://cdn.kolesa-darom.ru/"
link_CDN_2 = "https://cdn2.kolesa-darom.ru/"


link_DEV1_pipe = "https://" + os.getenv("HTTP_PIPE") + "dev1-pipe.kolesa-darom.ru/"
link_DEV2_pipe = "https://" + os.getenv("HTTP_PIPE") + "dev2-pipe.kolesa-darom.ru/"
link_DEV_pipe = "https://" + os.getenv("HTTP_PIPE") + "dev-pipe.kolesa-darom.ru/"
link_STAGE_pipe = "https://" + os.getenv("HTTP_PIPE") + "stage-pipe.kolesa-darom.ru/"
link_PIPE = "https://pipe.kolesa-darom.ru/"
link_B2B = "https://dev-b2b.kolesa-darom.ru/"


# """ Запись переменнных окружения в ini"""
# config = configparser.ConfigParser()
# config['testit'] = {}
# config['testit']['URL'] = os.getenv("TESTIT_URL")
# config['testit']['privateToken'] = os.getenv("TESTIT_privateToken")
# config['testit']['projectId'] = os.getenv("TESTIT_projectId")
# config['testit']['configurationId'] = os.getenv("TESTIT_configurationId")
# config['testit']['adapterMode'] = "2"
# with open('connection_config.ini', 'w') as cfgfile:
#     config.write(cfgfile)

""" Логирование """
logger = logging.getLogger(__name__)
# logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO, filename="test.log")


# Логи
class SeleniumListener(AbstractEventListener):
    # def before_find(self, by, value, browser):
    #     logging.info(f"Ищу: '{value}' по '{by}'")
    # def after_find(self, by, value, browser):
    #     logging.info(f"Нашел: '{value}' по '{by}'")
    # def before_click(self, element, browser):
    #     logging.info(f"Нажимаем на: {element}")
    # def after_click(self, element, browser):
    #     logging.info(f"Нажал на: {element}")
    # def before_quit(self, browser):
    #     logging.info(f"Закрываю браузер: {browser}")
    # def after_quit(self, browser):
    #     logging.info(f"Браузер закрыт")
    def on_exception(self, exception, browser):
        # logger.error(f"Ошибка: {exception}")
        allure.attach(browser.get_screenshot_as_png(), name=f"0_error_{browser.name}" + time.strftime("_%d_%b_%H:%M") +
                                                            ".png", attachment_type=allure.attachment_type.PNG)


def pytest_addoption(parser):
    parser.addoption('--local', help='Локально или CI?', choices=['true', 'false'], default='true')
    parser.addoption("--prod", help='Какой домен боевой?', default=link_WEB)
    parser.addoption("--link", help='Какой домен?', default=link_DEV_pipe)
    parser.addoption("--cdn", help='Какой домен CDN?', default=link_CDN_2)


@pytest.fixture(scope='session')
def local(request):
    return request.config.getoption('--local')


@pytest.fixture(scope='session')
def url(request):
    return request.config.getoption('--link')


options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Запуск браузера в фоновом режиме, без обычного запуска хрома
options.add_argument("--no-sandbox")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Убирает уведомление о работе хрома
# options.add_argument('--disable-popup-blocking')  # Убирает всплывающую фигню типа уведомлений хрома

@pytest.fixture(scope="function", params=["chrome"])
def browser_desktop(request, local, url):
    local = request.config.getoption("--local")
    url = request.config.getoption("--link")
    prod_url = request.config.getoption("--prod")

    if local == "true":
        #browser = webdriver.Chrome()
        #browser = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=options.to_capabilities())
        browser = webdriver.Chrome(ChromeDriverManager().install())
    elif local == "false":
        browser = webdriver.Chrome("/opt/selenoid-master/chromedriver", options=options)
    else:
        raise ValueError(f'Локально или CI не указан, --local="{local}"')

    browser = EventFiringWebDriver(browser, SeleniumListener())
    with allure.step(f"Запуск браузера '{browser.name}'"):
        browser.set_window_size(1920, 1080)
        browser.maximize_window()
        browser.implicitly_wait(5)
        browser.url, browser.prod_url = url, prod_url
        allure.attach(name="config", body=f"'stage': {url}\n'prod': {prod_url}", attachment_type=allure.attachment_type.TEXT)

        def final():
            try:
                allure.attach(name=browser.name, body=str(browser.desired_capabilities), attachment_type=allure.attachment_type.JSON)
                # allure.attach(name="log", body=browser.get_log('browser'), attachment_type=allure.attachment_type.TEXT)
            except TypeError as error:
                logger.error(f"Ошибка: {error}")
            finally:
                with allure.step(f"Закрываем браузер '{browser.name}'"):
                    browser.close()
                    browser.quit()
        request.addfinalizer(final)
    return browser


@pytest.fixture(scope="function", params=["chrome"])
def browser_mobile(request, local, url):
    local = request.config.getoption("--local")
    url = request.config.getoption("--link")
    prod_url = request.config.getoption("--prod")

    mobile_emulation = {"deviceName": "iPhone X"}
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")  # Запуск браузера в фоновом режиме, без обычного запуска хрома
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Убирает уведомление о работе хрома
    # chrome_options.add_argument('--disable-popup-blocking')  # Убирает всплывающую фигню типа уведомлений хрома


    if local == "true":
        browser = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=chrome_options.to_capabilities())
        #browser = webdriver.Chrome()
    elif local == "false":
        browser = webdriver.Chrome("/opt/selenoid-master/chromedriver", options=options, desired_capabilities=chrome_options.to_capabilities())
    else:
        raise ValueError(f'Локально или CI не указан --local="{local}"')

    browser = EventFiringWebDriver(browser, SeleniumListener())
    with allure.step(f"Запуск браузера '{browser.name}'"):
        browser.set_window_size(516, 1000)
        browser.implicitly_wait(5)
        browser.url, browser.prod_url = url, prod_url
        allure.attach(name="config", body=f"'stage': {url}\n'prod': {prod_url}", attachment_type=allure.attachment_type.TEXT)

        def final():
            try:
                allure.attach(name=browser.name, body=str(browser.desired_capabilities), attachment_type=allure.attachment_type.JSON)
                # allure.attach(name="log", body=browser.get_log('browser'), attachment_type=allure.attachment_type.TEXT)
            except TypeError as error:
                logger.error(f"Ошибка: {error}")
            finally:
                with allure.step(f"Закрываем браузер '{browser.name}'"):
                    browser.close()
                    browser.quit()
        request.addfinalizer(final)
    return browser


class ApiClient:
    def __init__(self, base_address, cdn_address):
        self.base_address = base_address
        self.cdn_address = cdn_address

    def get(self, path="/", params=None, cookies=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f"GET запрос на: {path}"):
            return requests.get(url=url, params=params, headers=headers, cookies=cookies, timeout=10, verify=False)

    def get_cdn(self, path="/", params=None, cookies=None, headers=None):
        url = f"{self.cdn_address}{path}"
        with allure.step(f"GET запрос на: {path}"):
            return requests.get(url=url, params=params, headers=headers, cookies=cookies, timeout=10, verify=False)

    def post(self, path="/", params=None, data=None, json=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f"POST запрос на: {path}"):
            return requests.post(url=url, params=params, data=data, json=json, headers=headers, timeout=10, verify=False)

    def delete(self, path="/", params=None, data=None, json=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f"DELETE запрос на: {path}"):
            return requests.delete(url=url, params=params, data=data, json=json, headers=headers, timeout=10, verify=False)

    def put(self, path="/", params=None, data=None, json=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f"PUT запрос на: {path}"):
            return requests.put(url=url, params=params, data=data, json=json, headers=headers, timeout=10, verify=False)


@pytest.fixture(scope="session")
def api_client(request, url):
    url = request.config.getoption("--link")
    if url == link_UAT:
        return ApiClient(base_address=link_UAT, cdn_address=link_CDN_UAT)
    elif url == link_EXTERNAL:
        return ApiClient(base_address=link_EXTERNAL, cdn_address=link_CDN_EXTERNAL)
    elif url == link_FEED1:
        return ApiClient(base_address=link_FEED1, cdn_address=link_CDN_2)
    elif url == link_FEED1_2:
        return ApiClient(base_address=link_FEED1_2, cdn_address=link_CDN_2)
    elif url == link_FEED2:
        return ApiClient(base_address=link_FEED2, cdn_address=link_CDN_2)
    elif url == link_FEED2_2:
        return ApiClient(base_address=link_FEED2_2, cdn_address=link_CDN_2)
    elif url == link_WEB_BOT1:
        return ApiClient(base_address=link_WEB_BOT1, cdn_address=link_CDN_2)
    elif url == link_WEB_BOT1_2:
        return ApiClient(base_address=link_WEB_BOT1_2, cdn_address=link_CDN_2)
    elif url == link_WEB_BOT2:
        return ApiClient(base_address=link_WEB_BOT2, cdn_address=link_CDN_2)
    elif url == link_WEB_BOT2_2:
        return ApiClient(base_address=link_WEB_BOT2_2, cdn_address=link_CDN_2)
    elif url == link_WEB4:
        return ApiClient(base_address=link_WEB4, cdn_address=link_CDN_2)
    elif url == link_WEB4_2:
        return ApiClient(base_address=link_WEB4_2, cdn_address=link_CDN_2)
    elif url == link_WEB3:
        return ApiClient(base_address=link_WEB3, cdn_address=link_CDN_2)
    elif url == link_WEB3_2:
        return ApiClient(base_address=link_WEB3_2, cdn_address=link_CDN_2)
    elif url == link_WEB2:
        return ApiClient(base_address=link_WEB2, cdn_address=link_CDN_2)
    elif url == link_WEB2_2:
        return ApiClient(base_address=link_WEB2_2, cdn_address=link_CDN_2)
    elif url == link_WEB1:
        return ApiClient(base_address=link_WEB1, cdn_address=link_CDN_2)
    elif url == link_WEB1_2:
        return ApiClient(base_address=link_WEB1_2, cdn_address=link_CDN_2)
    elif url == link_WEB:
        return ApiClient(base_address=link_WEB, cdn_address=link_CDN_2)
    elif url == link_DEV1_pipe:
        return ApiClient(base_address=link_DEV1_pipe, cdn_address=link_CDN_2)
    elif url == link_DEV2_pipe:
        return ApiClient(base_address=link_DEV2_pipe, cdn_address=link_CDN_2)
    elif url == link_DEV_pipe:
        return ApiClient(base_address=link_DEV_pipe, cdn_address=link_CDN_2)
    elif url == link_STAGE_pipe:
        return ApiClient(base_address=link_STAGE_pipe, cdn_address=link_CDN_2)
    elif url == link_PIPE:
        return ApiClient(base_address=link_PIPE, cdn_address=link_CDN_2)
    else:
        raise ValueError(f"Ссылка не указана --link='{url}'")
