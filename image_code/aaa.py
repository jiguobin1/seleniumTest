# coding：utf-8
#author：jiguobin

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


driver=webdriver.Chrome()
driver.get('http://192.168.19.25:8000/cms/login.in')

# driver.find_element_by_id("logInName").send_keys('jrpt')
# driver.find_element_by_id("password").send_keys('111qqq')


