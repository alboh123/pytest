# Generated by Selenium IDE
from idlelib import browser
from telnetlib import EC

import allure
import requests
import pytest
import time
import json
import unittest

from _pytest import unittest
from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, TimeoutException, \
    NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import unittest
from selenium import webdriver
class test_case1(unittest.TestCase):
    @allure.epic('Класс автотестов для сравнения')
    @allure.feature('Сравнение значения двух строк')
    @allure.story('Особенный автотест')
    @allure.title('Этот автотест проверяет важную фичу')
    @allure.description('Это описание нам поможет понять че там в тесте происходит')
    @allure.issue('https://www.google.ru/')
    @allure.issue('https://www.google.ru/', name= 'Это какой-то issue')
    @allure.tag('tag1')
    @allure.tag('tag2')
    @allure.tag('tag3')
    @allure.link('https://www.google.ru/', name= 'Это какая-то ссылка')
    @allure.severity("critical")
    @allure.severity("blocker")
    @allure.parent_suite("test_case1")
    @allure.sub_suite('test_case2')
    @allure.suite('это какой-то сьют')
    @allure.testcase("https://omni.top-academy.ru/login/index#/", name="это какой-то тест-кейс")


    @allure.description_html('<h2>Дополнительная информация:</h2><li>Этот тест проверяет ...<li>')


    def test1(self):
        s1 ="Rub"
        s2 ="Rub"
        # Verifying Numbers

        self.assertTrue(s1 == s2, "It's not a Match.")

    @allure.step('Шаг2')
    @allure.feature('Сравнение значения двух строк, вариант 2')
    def test2(self):
        s1 ="Rub"
        s2 ="Rub"
        # Verifying Numbers
        self.assertTrue(s1 == s2, "It's not a Match.")
    def test3(self):
        s1 ="Rub"
        s2 ="Rub"
        # Verifying Numbers
        self.assertTrue(s1 == s2, "It's not a Match.")
class test_case2(unittest.TestCase):
    @allure.feature('Open')
    def test2(self):
        s1 ="Ruby"
        s2 ="Ruby"
        # Verifying Numbers
        self.assertEquals(s1 == s2, "It's not a Match.")
