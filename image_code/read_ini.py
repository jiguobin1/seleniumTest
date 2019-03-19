#coding=utf-8
#author：jiguobin
#pip install Configparser

#D:\liantuo\seleniumTest\config\LocalElement.ini
# 参数中增添：encoding='UTF-8' 防止（UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 15: illegal multibyte sequence）
#稍后学习这个
import configparser
import os

# cf=configparser.ConfigParser()
# cf.read('E:\Pythonx\seleniumTest\config\LocalElement.ini',encoding='UTF-8')
# # print(cf.sections())#获取配置文件中所有节点
# #print(cf.options("LoginElement"))  #获取节点下所有。。
# print(cf.get('LoginElement','user_name'))

class ReadIni(object):
     # 构造函数
    def __init__(self,file_name=None,node=None):
        if file_name == None:
            file_name = 'E:\Pythonx\seleniumTest\config\LocalElement.ini'
        else:
            self.file_name=file_name
        if node == None:
            self.node = "LoginElement"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)
    #加载文件
    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name,encoding='utf-8')
        return cf

    #获取value得值
    def get_value(self,key):
        data = self.cf.get(self.node,key)
        return data


if __name__ == '__main__':
    path=r'E:\Pythonx\seleniumTest\config\testIni.ini'
    read_init = ReadIni(file_name=path,node='testa')
    print(read_init.get_value('ji'))



