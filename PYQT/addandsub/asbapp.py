import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from asbui import *


class asb(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)       
        self.ui.pushButton.clicked.connect(self.add)
        self.ui.pushButton_2.clicked.connect(self.sub)
        self.ui.pushButton_3.clicked.connect(self.reset)
        self.show()
    def add(self):
       self.n1=(self.ui.lineEdit.text())
       self.n2=(self.ui.lineEdit_2.text())
       self.res=(int(self.n1))+(int(self.n2))
       self.ui.label_4.setText("%d"%self.res)
    def sub(self):
       self.n1=int(self.ui.lineEdit.text())
       self.n2=int(self.ui.lineEdit_2.text())
       self.res=(int(self.n1))-(int(self.n2))
       self.ui.label_4.setText("%d"%self.res)
    def reset(self):
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit.setText("")
        self.ui.label_4.setText("")
        

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = asb()
    w.show()
    sys.exit(app.exec_())
