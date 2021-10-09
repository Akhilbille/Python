import sys
import mysql.connector
from datetime import date
from PyQt5.QtWidgets import QMainWindow,QApplication
from SPMUi import *

class SuperMarket(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.stockEntry)
        self.ui.pushButton_5.clicked.connect(self.reset)
        self.ui.pushButton_6.clicked.connect(self.exit)
        self.ui.pushButton.clicked.connect(self.arrivalDate)
        self.ui.pushButton_2.clicked.connect(self.mfgDate)
        self.ui.pushButton_3.clicked.connect(self.expDate)
        self.ui.comboBox_2.currentIndexChanged.connect(self.showProducts)
        self.ui.pushButton_7.clicked.connect(self.showProductstoUpdate)
        self.ui.pushButton_8.clicked.connect(self.updateProducts)
        self.ui.pushButton_9.clicked.connect(self.deleteProducts)
        
    def reset(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_8.clear()
        
    def exit(self):
        sys.exit()
    def arrivalDate(self):
        self.date=self.ui.calendarWidget.selectedDate()
        self.ui.lineEdit_6.setText(self.date.toString("yyyy/MM/dd"))
    def mfgDate(self):
        self.date=self.ui.calendarWidget.selectedDate()
        self.ui.lineEdit_7.setText(self.date.toString("yyyy/MM/dd"))
    def expDate(self):
        self.date=self.ui.calendarWidget.selectedDate()
        self.ui.lineEdit_8.setText(self.date.toString("yyyy/MM/dd"))
    def stockEntry(self):
        pid=int(self.ui.lineEdit.text())
        pc=self.ui.lineEdit_2.text()
        pname=self.ui.lineEdit_3.text()
        quan=int(self.ui.lineEdit_4.text())
        price=float(self.ui.lineEdit_5.text())
        da=self.ui.lineEdit_6.text()
        dm=self.ui.lineEdit_7.text()
        de=self.ui.lineEdit_8.text()
        place=self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
        sql="insert into products(productId,productCode,productName,quantity,price,doa,dom,doe,mfgplace) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(pid,pc,pname,quan,price,da,dm,de,place)
        cur.execute(sql,val)
        myconn.commit()
        QtWidgets.QMessageBox.about(self,"Success","Sucessfully Inserted")
        self.statusBar().showMessage('Sucessfully Inserted')
        self.reset()
    def showProducts(self):
        var=self.ui.comboBox_2.itemText(self.ui.comboBox.currentIndex())
        myconn=mysql.connector.connect(host="localhost", user="root",password="naveen",database="spm")
        cur = myconn.cursor()
        cur.execute("select * from products")
        res=cur.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for r_no, r_data in enumerate(res):
            self.ui.tableWidget.insertRow(r_no)
            for c_no, data in enumerate(r_data):
                self.ui.tableWidget.setItem(r_no,c_no,QtWidgets.QTableWidgetItem(str(data)))
        myconn.close()
    def showProductstoUpdate(self):
        id=int(self.ui.lineEdit.text())
        myconn=mysql.connector.connect(host="localhost", user="root",password="naveen",database="spm")
        cur = myconn.cursor()
        sql="select * from products where productId=%s"
        val=[(id)]
        cur.execute(sql,val)
        res=cur.fetchone()
        print(res)
        self.ui.lineEdit_2.setText(res[1])
        self.ui.lineEdit_3.setText(res[2])
        self.ui.lineEdit_4.setText(str(res[3]))
        self.ui.lineEdit_5.setText(str(res[4]))
        self.ui.lineEdit_6.setText(date.isoformat(res[5]))
        self.ui.lineEdit_7.setText(date.isoformat(res[6]))
        self.ui.lineEdit_8.setText(date.isoformat(res[7]))
        myconn.close()
    def updateProducts(self):
        pid=int(self.ui.lineEdit.text())
        pc=self.ui.lineEdit_2.text()
        pname=self.ui.lineEdit_3.text()
        quan=int(self.ui.lineEdit_4.text())
        price=float(self.ui.lineEdit_5.text())
        da=self.ui.lineEdit_6.text()
        dm=self.ui.lineEdit_7.text()
        de=self.ui.lineEdit_8.text()
        place=self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
        sql="update products set productCode=%s,productName=%s,quantity=%s,price=%s,doa=%s,dom=%s,doe=%s,mfgplace=%s where productId=%s"
        val=(pc,pname,quan,price,da,dm,de,place,pid)
        cur.execute(sql,val)
        myconn.commit()
        QtWidgets.QMessageBox.about(self,"Success","Sucessfully Updated")
        self.statusBar().showMessage('Sucessfully Updated')
        self.reset()
        myconn.close()
    def deleteProducts(self):
        id=int(self.ui.lineEdit_9.text())
        myconn=mysql.connector.connect(host="localhost", user="root",password="naveen",database="spm")
        cur = myconn.cursor()
        sql="delete from products where productId=%s"
        val=[(id)]
        cur.execute(sql,val)
        QtWidgets.QMessageBox.about(self,"Success","Record Deleted")
        self.statusBar().showMessage('Record Deleted')
        myconn.commit()
        myconn.close()
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = SuperMarket()
    myconn = mysql.connector.connect(host = "localhost", user = "root",password = "naveen",database = "spm")  
    cur = myconn.cursor()
    w.show()
    sys.exit(app.exec_())
