#coding=utf-8
#author：jiguobin
#pip install Configparser

#D:\liantuo\seleniumTest\config\LocalElement.ini
# 参数中增添：encoding='UTF-8' 防止（UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 15: illegal multibyte sequence）
import configparser
class ReadIni(object):
    def __init__(self,file_name=None,node=None):
        if file_name == None:
            file_name = "D:\liantuo\seleniumTest\config\LocalElement.ini"
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
   read_init = ReadIni()
   print(read_init.get_value('user_name'))



