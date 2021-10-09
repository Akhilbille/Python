import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import mysql.connector
from FlamesUi import *


class Flames(QMainWindow):
    counter=1
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)       

        self.ui.pushButton.clicked.connect(self.check)
        self.ui.pushButton_2.clicked.connect(self.reset)
        self.show()

    def check(self):
        self.n1=(self.ui.lineEdit.text().lower()).replace(" ","")
        self.n2=(self.ui.lineEdit_2.text().lower()).replace(" ","")
        b_name=self.n1
        g_name=self.n2
        id_fl=Flames.counter
        Flames.counter+=1
        self.flames=['Friendship','Love','Affection','Marriage','Enemy','Siblings']
        for i in self.n1:
           for j in self.n2:
                if i==j:
                   self.n1=self.n1.replace(i,'',1)
                   self.n2=self.n2.replace(j,'',1)
                   break
        self.count=len(self.n1+self.n2)
        print("Count : ",self.count)
        if self.count>0:
           while len(self.flames)>1:
               self.c=self.count%len(self.flames)
               self.index=self.c-1
               if self.index>=0:
                   self.left=self.flames[:self.index]
                   self.right=self.flames[self.index+1:]
                   self.flames=self.right+self.left
               else:
                   self.flames=self.flames[:len(self.flames) - 1]
           
           QtWidgets.QMessageBox.about(self,"Result"," Relationship : {}".format(self.flames[0]))
           rel=self.flames[0]
           sql="insert into flames(b_name,g_name,rel) values(%s,%s,%s)"
           val=(b_name,g_name,rel)
           cur.execute(sql,val)
           myconn.commit()
           myconn.close()
        else:
            QtWidgets.QMessageBox.about(self,"Result"," Flames can't be checked for same Names")
            sql="insert into flames(b_name,g_name,rel) values(%s,%s,%s)"
            rel="not possible on same names"
            val=(b_name,g_name,rel)
            cur.execute(sql,val)
            myconn.commit()
            myconn.close()

    def reset(self):
        self.ui.lineEdit.setText('')
        self.ui.lineEdit_2.setText('')
      
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    myconn = mysql.connector.connect(host = "localhost", user = "root",password = "",database = "flames")  
    cur = myconn.cursor()
    w = Flames()
    w.show()
    sys.exit(app.exec_())
