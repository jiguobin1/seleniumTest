# coding：utf-8
#author：jiguobin

from selenium import webdriver
import time
import random
#pip install pillow
from PIL import Image
from image_code.ShowapiRequest import ShowapiRequest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()

#浏览器初始化
def driver_init():
    driver.get('http://cms.liantuobank.com/cms/login.in')
    # driver.maximize_window()
    time.sleep(1)

#获取元素信息
def get_element(id):
    element=driver.find_element_by_id(id)
    return element

#获取随机数
def get_random():
    user_info=''.join(random.sample('9843958dhkjfhjksdhfkshd',5))
    return user_info

#获取图片
def get_code_image(fiel_name):
    driver.save_screenshot(fiel_name)
    code_element=driver.find_element_by_id('verifyCode')
    left=code_element.location['x']
    top=code_element.location['y']
    right=code_element.size['width']+left
    height=code_element.size['height']+top
    im=Image.open(fiel_name)
    img=im.crop((left,top,right,height))
    img.save(fiel_name)

#解析图片获取验证码
def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
    r.addBodyPara("typeId", "14")
    r.addBodyPara("convert_to_jpg", "0")
    r.addFilePara("image", file_name) #文件上传时设置
    res = r.post()
    print(res.text)
    text = res.json()['showapi_res_body']['Result']
    return text

#判断元素是否存在
def is_element(id):
    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,id)))
    except:
        return False
    else:
        return True

#流程入口
def run_main():
    #文件路径
    file_name = "D:test02.png"
    driver_init()
    get_element("logInName").send_keys('xuqiandls')
    get_element("password").send_keys('111qqq')
    get_code_image(file_name)
    text = code_online(file_name)
    get_element("verifyCodeInput").send_keys(text)
    get_element("submitForm").click()
    #.text获取元素文本值
    error_code=get_element('errorVerifyCode').text
    if error_code=='验证码输入错误':
        get_code_image(file_name)
        text = code_online(file_name)
        time.sleep(2)
        get_element("verifyCodeInput").send_keys(text)
        get_element("submitForm").click()


run_main()

