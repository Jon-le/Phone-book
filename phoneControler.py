# -*- coding: utf-8 -*-
__author__ = 'Иван'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class Controler:
    def __init__(self,model):
        self._model = model
        self.initContriler()
    def setView(self,viev):
        self._view = viev
        self._view.initMain()
        self.listDataTreeview = self._model.getDataTreeView()
        self._view.viewTree(self.listDataTreeview)
    def initContriler(self):
        self._model.readAllData()
    def savePhone(self,name,phone):

        if(name != ''and name != ''and phone != ''or phone != '' ):
            status = self._model.saveData(name.decode("utf-8").encode('cp1251'),phone)
            self._view.addContact.status_Text(status)
            if( status[0] == 0):
                self.listDataTreeview = self._model.getDataTreeView()
                self._view.viewTree(self.listDataTreeview)
