import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from RandomNameGeneratorUi import *
from random import *

class RandomName(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)       
        self.ui.pushButton.clicked.connect(self.randomName)
    def randomName(self):
        l=[]
        f=open('players.txt','r')
        for i in f:
            l.append(i.strip('\n'))
        self.ui.label_2.setText(choice(l))
        f.close()
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = RandomName()
    w.show()
    sys.exit(app.exec_())
