#coding=utf-8
#author：jiguobin
'''
定位元素封装
'''
from util.read_ini import ReadIni
print('why')
# read_ini=ReadIni()
# data=read_ini.get_value('user_name')
# print(data)
# print(data.split('>'))
class FindElement(object):
    def __init__(self,driver):
        self.driver=driver
    #定位元素
    def get_element(self,key):
        read_ini=ReadIni()
        data=read_ini.get_value(key)
        by=data.split('>')[0]   #定位方式
        value=data.split('>')[1]  #定位值
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by =='className':
                return self.driver.find_element_by_class_name(value)
            elif by == 'linkText':
                return self.driver.find_element_by_link_text(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return None

