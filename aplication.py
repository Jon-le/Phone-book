# -*- coding: utf-8 -*-
from ttk import Treeview
import readPhone
import writePhone
import faleManager
import model
from  Tkinter import *
import PIL.Image
import PIL.ImageTk
import phoneControler
__author__ = 'Иван'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
"""
Приложения для сохранения телефонов в текстовий файл.
Прилодения реалызовано с помощу Tkinter
Имеет функцыонал для добавления телефонов и поиска по ID,name,phone
"""
class App:
    def __init__(self,model,controler):
        """
        Инициалызируем модель,контролер и передайом в контролер нашу view
        """
        self._model = model
        self.controler = controler
        self.controler.setView(self)
    def createFrame(self):
        """
        Создайом наше главное окно
        """
        self.root = Tk()
        self.root.title(u"Контакти")
        # розмер окна
        self.root.geometry("620x620")
        # запрещаю изменять розмер окна
        self.root.resizable(False,False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    def createToolBar(self):
        """
        Создайом бар сверху нашего окна
        """
        self.toolbar = Frame(bg = "#d7d8e0", bd = 2)
        self.toolbar.pack(side = TOP,fill = X)
    def createAddImgBttn(self):
        """
        Кнопка добавить
        """
        self.add_img = PIL.Image.open("add_phone_smoll.png")
        self.add_photo = PIL.ImageTk.PhotoImage(self.add_img)
        self.bttn_add_phone = Button(self.toolbar,text = u"Додати номер",command = self.initForm,bg ="#d7d8e0",bd = 0,compound = TOP,image = self.add_photo )
        self.bttn_add_phone.pack(side = LEFT)
    def createFindImgBttn(self):
        """
        Кнопка найти
        """
        self.find_img = PhotoImage(file = "depositphotos_29684905-stock-illustration-loupe81x65.gif")
        self.bttn_find_phone = Button(self.toolbar,text = u"Найти номер",command = self.findBttnEvent,bg ="#d7d8e0",bd = 0,compound = TOP,image = self.find_img )
        self.bttn_find_phone.pack(side = LEFT)
    def createTreeView(self):
        """
        Таблица с нашими даными
        """
        self.tree = Treeview(self.root,column = ('ID','Name','Phone'),height = 620,show = 'headings')
        self.tree.column('ID',width = 206,anchor = CENTER)
        self.tree.column('Name',width = 206,anchor = CENTER)
        self.tree.column('Phone',width = 206,anchor = CENTER)
        self.tree.heading('ID',text = "ID")
        self.tree.heading('Name',text = u"Имя")
        self.tree.heading('Phone',text = u"Номер телефону")
        self.tree.pack()
    def createScrollbar(self):
        """
        Создайом скрол и подвязываем наш скрол к нашей таблице
        """
        self.scroll = Scrollbar(orient="vertical",command= self.tree.yview)
        self.tree.configure(yscrollcommand=self.scroll.set)
        self.scroll.pack( side = RIGHT, fill = Y )
    def initForm(self):
        """
        События нажатия кнопки добавить контакт
        При нажатии создайом дочернее окно
        """
        self.addContact = AddContact(self)
    def findBttnEvent(self):
        """
        События кнопки найти контакт

        При нажатии создайот дочернее окно
        """
        FindContact(self)
    def initMain(self):
        """
        Функция которая создайот все окно
        """
        self.createFrame()
        self.createToolBar()
        self.createAddImgBttn()
        self.createFindImgBttn()
        self.createTreeView()
    def on_closing(self):
        """
        События закрытия главного окна
        Пры закрытии окна мы закрываем файл в который мы сохраяем нашы вконтакты
        """
        self.root.destroy()
        faleManager.FileManager().closeFale()
    def refresh(self,name,phone):
        self._read_phone.addData(name,phone)
        dict = self.read_phone.getData()
        list = []
        count = 1
        for key, value in dict.items():
            list2 = []
            list2.append(count)
            list2.append(value)
            list2.append(key)
            list.append(list2)
            count+=1
        [self.tree.delete(i) for i in self.tree.get_children()]
        #[self.tree.insert('','end',values = unicode(row)) for row in list]
        for i in list:
            print type(i[0])
            print type(i[1])
            print type(i[2])
            self.tree.insert('','end',values = (i[0],i[1].decode('cp1251').encode("utf-8"),i[2]))
    def viewTree(self,list):
        """
        Наполняем нашу таблицу даными
        """
        print self.tree
        [self.tree.delete(i) for i in self.tree.get_children()]
        for i in list:
            print type(i[0])
            print type(i[1])
            print type(i[2])
            self.tree.insert('','end',values = (i[0],i[1].encode("utf-8"),i[2]))
"""
Наше дочернее окно для добавления контакта
"""
class AddContact():
    def __init__(self,app):
        """
        Инициализируем наше дочерне окно передайом сылку главного окна
        Создайом наше окно
        """
        self.view = app
        self.initForm()
    def initForm(self):
        """
        Создайом наше окно
        """
        self.root = Toplevel()
        self.root.title(u"Введіть номер телефона")
        self.root.geometry("300x200")
        self.root.resizable(False,False)
        self.root.grab_set()
        self.root.focus_set()

        self.lable_Name = Label(self.root,text = u'Введить имя вконтака')
        self.lable_Name.place(x = 20,y = 0)

        self.entriName = Entry(self.root)
        self.entriName.place(x = 20,y = 20)

        self.lable_Phon = Label(self.root,text = u'Введить номер телефона')
        self.lable_Phon.place(x = 20,y = 60)

        self.entriPhone = Entry(self.root)
        self.entriPhone.place(x = 20,y = 80)

        self.bttn_save = Button(self.root,text = u'Зберегти',command = self.save_form)
        self.bttn_save.place(x = 170,y = 150)
        self.decoration_img = PIL.Image.open("decoration_img.png")
        self.photo = PIL.ImageTk.PhotoImage(self.decoration_img)
        self.label_img = Label(self.root, image=self.photo)
        self.label_img.place(x = 180,y = 10)

    def save_form(self):
        """
        События кнопки Сохранить
        Мы сохраняем дани в модель и записиваем в файл
        """
        if hasattr(self, 'statusLabel'):
            self.statusLabel.destroy()
        self.view.controler.savePhone(self.entriName.get(),self.entriPhone.get())
        """
        if(self.entriName.get() != ''and self.entriName.get() != ''and self.entriPhone.get() != ''or self.entriPhone.get() != '' ):
            wh = writePhone.WritePhone(self.entriName.get().decode("utf-8").encode('cp1251'),self.entriPhone.get())
            self.status_Text(wh)
            if(wh.getStatus() == 0):
                self.view.refresh(self.entriName.get().decode("utf-8").encode('cp1251'),int(self.entriPhone.get()))
                self.entriPhone.delete(0,END)
                self.entriName.delete(0,END)
                wh = None
        """

    def status_Text(self,status):
        """

        """
        status_text = status[1]
        color_text ='#00ff00'
        if( status[0] != 0 ):
            color_text = '#a00000'
        self.statusLabel = Label(self.root,text = status_text,font=("Helvetica", 14),fg = color_text)
        self.statusLabel.place(x = 20,y = 100)
class FindContact:
     def __init__(self,app):
         self._app = app
         self.createForm()
     def createForm(self):
         self.root = Toplevel()
         self.root.title(u"Введіть номер телефона")
         self.root.geometry("250x200")
         self.root.resizable(False,False)
         self.root.grab_set()
         self.root.focus_set()

         self.dataLabel = Label(self.root,text = u'Введить діни для пошуку')
         self.dataLabel.place(x = 10,y = 0)

         self.dataEntry = Entry(self.root)
         self.dataEntry.place(x = 10,y = 20)

         self.var = IntVar()
         self.var.set(0)
         self.id_Radiobutton = Radiobutton(self.root,text="ID", variable=self.var, value=0)
         self.id_Radiobutton.place(x = 150, y = 20)

         self.name_Radiobutton = Radiobutton(self.root,text=u"Имя", variable=self.var, value=1)
         self.name_Radiobutton.place(x = 150, y = 40)

         self.phone_Radiobutton = Radiobutton(self.root,text=u"Телефон", variable=self.var, value=2)
         self.phone_Radiobutton.place(x = 150, y = 60)
         self.bttn_find = Button(self.root,text = u'Знайти',command = self.findEventBttn)
         self.bttn_find.place(x = 40,y = 50)
     def findEventBttn(self):
         if hasattr(self, 'findLabel'):
            self.findLabel.destroy()
         if(self.var.get() == 1):
             find = self._app._model.findName(self.dataEntry.get().encode("utf-8"))
             print(find)
             if(type(find) != int):
                 self.findLabel = Label(self.root,text = self.dataEntry.get().encode("utf-8") + " +"+find[1],font=("Helvetica", 14),fg = '#00ff00')
                 self.findLabel.place(x = 20,y = 80)
         elif(self.var.get() == 2):
             find = self._app._model.findPhone(self.dataEntry.get().encode("utf-8"))
             self.findLabel = Label(self.root,text = find[0][:len(find[0]) - 1] + " +"+find[1],font=("Helvetica", 14),fg = '#00ff00')
             self.findLabel.place(x = 20,y = 80)
if __name__ =='__main__':
    model = model.Model()
    controler = phoneControler.Controler(model)
    app =App(model,controler)
    app.root.mainloop()
