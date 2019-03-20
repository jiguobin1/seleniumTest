# coding：utf-8
#author：jiguobin
'''
登录界面的封装
'''
from selenium import webdriver
from util.find_element import FindElement
from PIL import Image
from image_code.ShowapiRequest import ShowapiRequest

class Login():
    def __init__(self,url,i):
        self.driver=self.init_driver(url,i)

    #初始化浏览器
    def init_driver(self,url,i):
        if i==1:
            driver=webdriver.Chrome()
        elif i==2:
            driver=webdriver.Firefox()
        else:
            driver=webdriver.Edge()
        driver.get(url)
        driver.maximize_window()
        return driver

    #输入用户信息
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)

    #定位用户信息
    def get_user_element(self,key):
        find_element=FindElement(self.driver)
        user_element=find_element.get_element(key)
        return user_element

    #获取图片
    def get_code_image(self,fiel_name):
        self.driver.save_screenshot(fiel_name)
        code_element=self.driver.find_element_by_id('verifyCode')
        left=code_element.location['x']
        top=code_element.location['y']
        right=code_element.size['width']+left
        height=code_element.size['height']+top
        im=Image.open(fiel_name)
        img=im.crop((left,top,right,height))
        img.save(fiel_name)

    #解析图片获取验证码
    def code_online(self,file_name):
        r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
        r.addBodyPara("typeId", "14")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name) #文件上传时设置
        res = r.post()
        print(res.text)
        text = res.json()['showapi_res_body']['Result']
        return text

    #流程控制
    def main(self,user_name,pass_word):
        file_name = "D:test01.png"
        self.send_user_info('user_name',user_name)
        self.send_user_info('user_password',pass_word)
        self.get_code_image(file_name)
        code_text=self.code_online(file_name)
        self.send_user_info('code_text',code_text)


#入口
if __name__ == '__main__':
        login = Login('http://192.168.19.25:8000/cms/login.in',1)
        login.main('dfj','dsf')


