# -*- coding: utf-8 -*-
__author__ = 'Иван'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class Data:
    def __init__(self,ID,name,phone):
        self._ID = ID
        self.__name = name
        self.__phone = phone
    def getName(self):
        return  self.__name
    def getPhone(self):
        return self.__phone
    def getID(self):
        return self._ID
    def checkName(self,value):
        if(self.__name ==value):
            return True
        return False
    def checkPhone(self,value):
        if(self.__phone == value):
            return True
        return False
