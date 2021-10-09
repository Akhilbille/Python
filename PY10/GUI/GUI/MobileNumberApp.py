import sys
import re
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *

from MobileNumberUi import *

class NumberCheck(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.verify)

    def verify(self):
        mobnum=self.ui.lineEdit.text()
        m=re.fullmatch('[6-9][0-9]{9}',mobnum)
        if m!=None:
            self.ui.label_2.setText('Valid Mobile Number')
        else:
            self.ui.label_2.setText('InValid Mobile Number')
        self.ui.lineEdit.clear()


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = NumberCheck()
    w.show()
    sys.exit(app.exec_())
