import sys
import re
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from NumberCheckUi import *

class NumberCheck(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)       
        self.ui.pushButton.clicked.connect(self.check)
        self.ui.pushButton_2.clicked.connect(self.reset)
        self.ui.exit.clicked.connect(self.exit1)
        
        self.show()
    def check(self):
        self.num = self.ui.lineEdit.text()
        s=re.fullmatch("[6-9]\d{9}",self.num)
        if s!=None:
            self.ui.label_2.setText("Valid Mobile Number")
            QtWidgets.QMessageBox.about(self,"Message","Valid Mobile Number")
           
        else:
               self.ui.label_2.setText("is not a Valid Mobile Number")  
               QtWidgets.QMessageBox.about(self,"message","Invalid Mobile Number")
            
    def reset(self):
        self.ui.lineEdit.setText('')
    def exit1(self):
        sys.exit()
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = NumberCheck()
    w.show()
    sys.exit(app.exec_())
