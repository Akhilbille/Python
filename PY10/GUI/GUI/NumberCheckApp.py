import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from EvenNumberUi import *

class NumberCheck(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)       
        self.ui.pushButton.clicked.connect(self.check)
        self.ui.pushButton_2.clicked.connect(self.reset)
        self.ui.pushButton_3.clicked.connect(self.exit)
        self.show()
    def reset(self):
        self.ui.lineEdit.clear()
    def exit(self):
        sys.exit()
    def check(self):
        num=int(self.ui.lineEdit.text())
        if num%2==0:
            #self.ui.label_2.setText("Even Number")
            QtWidgets.QMessageBox.about(self,"Result","Even Number")
        else:
            #self.ui.label_2.setText("Odd Number")
            QtWidgets.QMessageBox.about(self,"Result","Odd Number")

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = NumberCheck()
    w.show()
    sys.exit(app.exec_())
