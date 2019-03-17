# coding：utf-8
#author：jiguobin

from selenium import webdriver
from util.utils import *
#上传测试



driver=webdriver.Chrome()
driver.get('http://intcms.51ebill.com/cms/login.in')
print(is_title(driver,'dkjsf'))
print(is_tiele_contain(driver,'首页'))
print(is_element(driver,'logInNam'))
#
# driver.find_element_by_id("logInName").send_keys('jrpt')
# driver.find_element_by_id("password").send_keys('111qqq')


