import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from FileHandlerUi import *

class File(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)       
        self.ui.pushButton.clicked.connect(self.addText)
        self.ui.pushButton_2.clicked.connect(self.exit)
    def addText(self):
        f.write(self.ui.lineEdit.text()+'\n')
        self.ui.lineEdit.clear()
    def exit(self):
        sys.exit()
    
        

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = File()
    f=open('output.txt','a+')
    w.show()
    sys.exit(app.exec_())
