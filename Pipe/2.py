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

class base_page(self, url, )

# #    def go_to_site(self):
#             with allure.step("Открываем сайт"):
#             self.logger.info(f"Открываем сайт: {self.url}")
#             self.browser.get(self.url)
