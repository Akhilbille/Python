import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from FlamesUi import *

class Flames(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)       
        self.ui.pushButton.clicked.connect(self.check)
        self.ui.pushButton_2.clicked.connect(self.reset)

    def reset(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
    def check(self):
        n1=(self.ui.lineEdit.text().lower()).replace(" ","")
        n2=(self.ui.lineEdit_2.text().lower()).replace(" ","")
        flames=['Friendship','Love','Affection','Marriage','Enemy','Siblings']
        for i in n1:
             for j in n2: 
                 if i==j:
                   n1=n1.replace(i,'',1)
                   n2=n2.replace(j,'',1)
                   break
        count=len(n1+n2)
        print("Count : ",count)
        if count>0:
           while len(flames)>1:
                c=count%len(flames)
                index=c-1
                if index>=0:
                   left=flames[:index]
                   right=flames[index+1:]
                   flames=right+left
                else:
                    flames=flames[:len(flames) - 1]
           
           QtWidgets.QMessageBox.about(self,"Relationship",flames[0])
        else:
           
           QtWidgets.QMessageBox.about(self,"Relationship","FLAMES can't be checked for same Names")


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Flames()
    w.show()
    sys.exit(app.exec_())
