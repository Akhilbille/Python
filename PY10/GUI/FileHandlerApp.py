import sys

from PyQt5.QtWidgets import QMainWindow,QApplication
from FileHandlerUi import *

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.addData)
        self.ui.pushButton_2.clicked.connect(self.saveandexit)

    def addData(self):
        f.write(self.ui.lineEdit.text()+'\n')
        self.ui.lineEdit.clear()
    def saveandexit(self):
        f.close()
        sys.exit()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    f=open('text_file.txt','a+')
    w.show()
    sys.exit(app.exec_())
