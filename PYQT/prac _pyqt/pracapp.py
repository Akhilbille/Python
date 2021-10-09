import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from pracui import *


class prac(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)       
        self.ui.pushButton.clicked.connect(self.display)
        self.ui.pushButton_2.clicked.connect(self.reset)
        self.show()
    def display(self):
       self.name=self.ui.lineEdit.text()
       self.ui.label_3.setText(self.name)
    def reset(self):
        self.ui.label_3.setText("")
        self.ui.lineEdit.setText("")
        
        

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = prac()
    w.show()
    sys.exit(app.exec_())
