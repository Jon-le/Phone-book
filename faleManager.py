# -*- coding: utf-8 -*-
import codecs
__author__ = 'Иван'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class FileManager(object):
    __instance = None
    def __new__(cls):
        if FileManager.__instance is None:
            FileManager.__instance = object.__new__(cls)
        return FileManager.__instance
    def __init__(self):
        self._f = codecs.open('phone.txt', 'a+')
    def writeFile(self,name,phone):
        self._f.write(name)
        self._f.write(phone)
    def closeFale(self):
        self._f.close()
    def getFile(self):
        return self._f