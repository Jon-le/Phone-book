# -*- coding: utf-8 -*-
import phone_data
__author__ = 'Иван'
import sys
import faleManager
reload(sys)
sys.setdefaultencoding('utf-8')
class Model:
    def __init__(self):
        self.initModel()
    def initModel(self):
        self.__listData = []
    def readAllData(self):
        ID = 1
        count = 1;
        key = 0 # Ключом будуть наші телефони тому що вони унікальні
        value = "" # Значення це наші імена вкрнтаків
        # Перебираємо всі наші строки в текстовому документі
        for line in faleManager.FileManager().getFile():
            # Якщо це парна строка значід тут у нас телефон записуємо його ключом
            # І якщо у нас є і ключ і значення записуємо в словар
            if count %2 ==0:
                key = int(line)
                self.addData(ID,value.decode("cp1251").encode('utf-8'),str(key))
                ID+=1
            else:
                # Значення це наші всі імена вконтактів вони ідуть по непарним строкам
                value = line
            count+=1
    def getDataTreeView(self):
        list = []
        for i in range(len(self.__listData)):
            list2 = []
            list2.append(self.__listData[i].getID())
            list2.append(self.__listData[i].getName())
            list2.append(self.__listData[i].getPhone())
            list.append(list2)
        return list
    def getEND_ID(self):
        end_ID = 0
        for i in range(len(self.__listData)):
            if( self.__listData[i].getID() > end_ID ):
                end_ID = self.__listData[i].getID()
        return  end_ID
    def addData(self,ID,name,phone):
        self.__listData.append(phone_data.Data(ID,name,phone))
    def saveData( self, name, phone ):
        if(type( name )is  not str  ):
            print(type(name))
            print u"Name:Не вірні дані"
        elif(phone.isdigit()== False ):
            status = 1
            statusString = u'В номерв є літери'
            print u"Phone:Не вірні дані"
        else:
            if(self.findPhone(phone)!= 0):
                status = 2
                statusString = u'Такий телефон вже існує'
            else:
                status = 0
                statusString = u'Все вірно'
                self.addData(self.getEND_ID()+1,name,phone)
                faleManager.FileManager().writeFile(name+'\n',str(phone)+'\n')
        return status,statusString
    def findName(self,value):
        for i in range(len(self.__listData)):
            if(self.__listData[i].checkName(value+'\n')):
                return (self.__listData[i].getName(),self.__listData[i].getPhone())
        return 0
    def findPhone(self,value):
        for i in range(len(self.__listData)):
            if(self.__listData[i].checkPhone(value)):
                return (self.__listData[i].getName(),self.__listData[i].getPhone())
        return 0
