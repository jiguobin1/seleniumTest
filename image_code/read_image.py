#codinng=utf-8
import pytesseract
from PIL import Image
from image_code.ShowapiRequest import ShowapiRequest
# image = Image.open("D:/jdsz.png")
# text = pytesseract.image_to_string(image)
# print(text)

r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
r.addBodyPara("typeId", "14")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", r"D:/imooc1.png") #文件上传时设置
res = r.post()
print(res.text)
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息