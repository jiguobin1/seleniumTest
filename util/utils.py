# coding：utf-8
#author：jiguobin
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#验证标题是否存在（精准）
def is_title(driver,title):
    title=EC.title_is(title)
    return title(driver)

#验证标题是否包含存在
def is_tiele_contain(driver,title):
    title=EC.title_contains(title)
    return title(driver)

#通过id判断元素是否存在
def is_element(driver,element_id):
    try:
        #WebDriverWait(driver,查找时间)
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.ID,element_id)))
    except:
        return False
    else:
        return True
