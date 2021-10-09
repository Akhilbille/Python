import sys
import mysql.connector
from datetime import date
from PyQt5.QtWidgets import QMainWindow,QApplication
from super_marketui import *

class SPM(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.submit)
        self.ui.pushButton_2.clicked.connect(self.clear)
        self.ui.pushButton_3.clicked.connect(self.arrivalDate)
        self.ui.pushButton_4.clicked.connect(self.expireDate)
        self.ui.comboBox.currentIndexChanged.connect(self.places)
        self.show()
    def places(self):
        self.place=self.ui.comboBox.currentText()
    def arrivalDate(self):
        self.date=self.ui.calendarWidget.selectedDate()
        self.ui.lineEdit_12.setText(self.date.toString("yyyy/MM/dd"))
    def expireDate(self):
        self.date=self.ui.calendarWidget.selectedDate()
        self.ui.lineEdit_13.setText(self.date.toString("yyyy/MM/dd"))
    
    def submit(self):
        P_id=int(self.ui.lineEdit_2.text())
        P_name=self.ui.lineEdit_3.text()
        P_code=self.ui.lineEdit_5.text()
        P_price=float(self.ui.lineEdit_6.text())
        P_qty=int(self.ui.lineEdit_7.text())
        vendor=self.ui.lineEdit_8.text()
        mobile=self.ui.lineEdit_9.text()
        mfg_name=self.ui.lineEdit_10.text()
        mfg_place=self.place
        P_arrival=self.ui.lineEdit_12.text()
        P_exp=self.ui.lineEdit_13.text()
        sql="insert into stock(p_id,p_name,p_code,price,quantity,vendor,vendor_mob_num,mfg_name,mfg_place,date_of_arrival,exp_date)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
        val=(P_id,P_name,P_code,P_price,P_qty,vendor,mobile,mfg_name,mfg_place,P_arrival,P_exp)
        cur.execute(sql,val)
        myconn.commit()
        myconn.close()
        QtWidgets.QMessageBox.about(self,"Success","Sucessfully Inserted")
        self.statusBar().showMessage('Sucessfully Inserted')
        self.clear()
    def clear(self):
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_8.clear()
        self.ui.lineEdit_9.clear()
        self.ui.lineEdit_10.clear()
        
        self.ui.lineEdit_12.clear()
        self.ui.lineEdit_13.clear()
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = SPM()
    myconn = mysql.connector.connect(host = "localhost", user = "root",password = "naveen",database = "Super_market")  
    cur = myconn.cursor()
    w.show()
    sys.exit(app.exec_())
