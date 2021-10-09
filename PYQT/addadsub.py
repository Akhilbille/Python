import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from addsub import *


class addsub(QMainWindow):
    def _init_(self):
        super()._init_()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)       

        self.ui.pushButton_2.clicked.connect(self.add)
        self.ui.pushButton.clicked.connect(self.sub)
        self.show()

    def add(self):
	self.num1=int(self.ui.lineEdit.text())
	self.num2=int(self.ui.lineEdit_2.text())
	        
	









if _name=="main_":
    app = QApplication(sys.argv)
    w = addsub()
    w.show()
    sys.exit(app.exec_())