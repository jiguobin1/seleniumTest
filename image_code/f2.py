from selenium import webdriver
import time
# from PIL import Image
# from image_code.ShowapiRequest import ShowapiRequest
driver=webdriver.Chrome()
driver.get('http://192.168.19.25:8000/cms/login.in')
driver.find_element_by_id("logInName").send_keys('jrpt')
driver.find_element_by_id("password").send_keys('111qqq')

time.sleep(5)
driver.find_element_by_id('submitForm').click()
#获取元素值
errror_code=driver.find_element_by_id('errorVerifyCode').text
while errror_code=='验证码输入错误':
    time.sleep(5)
    print('验证码输入错误重新输入')
    driver.find_element_by_id('submitForm').click()






# driver.save_screenshot('D:/imooc.png')
# code_element=driver.find_element_by_id('verifyCode')
# left=code_element.location['x']
# top=code_element.location['y']
# right=code_element.size['width']+left
# height=code_element.size['height']+top
# im=Image.open('D:/imooc.png')
# img=im.crop((left,top,right,height))
# img.save('D:/imooc1.png')
#
# r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
# r.addBodyPara("typeId", "14")
# r.addBodyPara("convert_to_jpg", "0")
# r.addFilePara("image", r"D:/imooc1.png") #文件上传时设置
# res = r.post()
# text = res.json()['showapi_res_body']['Result']
# print(text) # 返回信息
# time.sleep(2)
# driver.find_element_by_id('verifyCodeInput').send_keys(text)











