import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from BillingUi import *


class Billing(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)       
        self.ui.pushButton.clicked.connect(self.billCode)
        self.ui.pushButton_2.clicked.connect(self.reset)
        self.ui.pushButton_3.clicked.connect(self.exitCode)
        self.show()
        
    def billCode(self):

        self.gm=self.gr=self.nd=self.end=self.mm=self.mfr=self.pfr=self.efr=self.cd=0
        self.bill=self.sgst=self.cgst=0
        self.gm=int(self.ui.lineEdit.text())*30
        self.gr=int(self.ui.lineEdit_2.text())*40
        self.nd=int(self.ui.lineEdit_3.text())*35
        self.end=int(self.ui.lineEdit_4.text())*45
        self.mm=int(self.ui.lineEdit_5.text())*50
        self.mfr=int(self.ui.lineEdit_6.text())*55
        self.pfr=int(self.ui.lineEdit_7.text())*60
        self.efr=int(self.ui.lineEdit_8.text())*45
        self.cd=int(self.ui.lineEdit_9.text())*20

        self.bill=self.gm+self.gr+self.nd+self.end+self.mm+self.mfr+self.pfr+self.efr+self.cd
        self.sgst= self.bill*0.09
        self.cgst= self.bill*0.09
        self.tot_bill=self.bill+self.sgst+self.cgst

        self.ui.label_15.setText('%.2f' %self.bill)
        self.ui.label_16.setText('%.2f' %self.sgst)
        self.ui.label_17.setText('%.2f' %self.cgst)
        self.ui.label_18.setText('%.2f' %self.tot_bill)
        
    def reset(self):
        self.ui.lineEdit.setText('')
        self.ui.lineEdit_2.setText('')
        self.ui.lineEdit_3.setText('')
        self.ui.lineEdit_4.setText('')
        self.ui.lineEdit_5.setText('')
        self.ui.lineEdit_6.setText('')
        self.ui.lineEdit_7.setText('')
        self.ui.lineEdit_8.setText('')
        self.ui.lineEdit_9.setText('')
        self.ui.label_15.setText('')
        self.ui.label_16.setText('')
        self.ui.label_17.setText('')
        self.ui.label_18.setText('')
    def exitCode(self):
        sys.exit()
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Billing()
    w.show()
    sys.exit(app.exec_())
