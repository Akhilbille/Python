import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from evenoradd import *
class even_odd(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)       
        self.ui.pushButton.clicked.connect(self.check)
        self.ui.pushButton_2.clicked.connect(self.clear)
        self.ui.pushButton_3.clicked.connect(self.exit)
        self.show()
    def check(self):
        num=int(self.ui.lineEdit.text())
        if num%2==0:
            self.ui.label_3.setText("EVEN NUMBER")
        else:
            self.ui.label_3.setText("ODD NUMBER")
    def clear(self):
        self.ui.lineEdit.clear()
        self.ui.label_3.clear()
    def  exit(self):
        self.ui.sys.exit()
    

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = even_odd()
    w.show()
    sys.exit(app.exec_())