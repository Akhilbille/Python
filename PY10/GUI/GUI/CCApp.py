import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from CCUi import *

class ChatCentre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.bill)
        self.ui.pushButton_2.clicked.connect(self.reset)
        self.ui.pushButton_3.clicked.connect(self.exit)
    def exit(self):
        sys.exit()
    def reset(self):
        self.ui.lineEdit_4.setText('0')
        self.ui.lineEdit_5.setText('0')
        self.ui.lineEdit_6.setText('0')
        self.ui.lineEdit_7.setText('0')
        self.ui.lineEdit_8.setText('0')
        self.ui.lineEdit_9.setText('0')
        self.ui.lineEdit_16.setText('0')
        self.ui.lineEdit_17.setText('0')
        self.ui.lineEdit_18.setText('0')

        self.ui.label_21.setText('')
        self.ui.label_22.setText('')
        self.ui.label_24.setText('')
        self.ui.label_26.setText('')
    def bill(self):
        pp=int(self.ui.lineEdit_4.text())
        bp=int(self.ui.lineEdit_5.text())
        gm=int(self.ui.lineEdit_6.text())
        ct=int(self.ui.lineEdit_7.text())
        mp=int(self.ui.lineEdit_8.text())
        dp=int(self.ui.lineEdit_9.text())
        en=int(self.ui.lineEdit_16.text())
        sf=int(self.ui.lineEdit_17.text())
        cd=int(self.ui.lineEdit_18.text())
        bill=pp*10+bp*20+gm*40+ct*30+mp*20+dp*30+en*40+sf*40+cd*20
        cgst=bill*0.09
        sgst=bill*0.09
        tot_bill=bill+cgst+sgst
        
        self.ui.label_21.setText(str(bill))
        self.ui.label_22.setText(str(cgst))
        self.ui.label_24.setText(str(sgst))
        self.ui.label_26.setText(str(tot_bill))

        
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = ChatCentre()
    w.show()
    sys.exit(app.exec_())
