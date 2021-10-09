import sys
import mysql.connector
from datetime import date
from PyQt5.QtWidgets import QMainWindow,QApplication
from textileUi import *

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.register)
        self.ui.pushButton_2.clicked.connect(self.reset)
        self.ui.pushButton_3.clicked.connect(self.exit)
        self.ui.pushButton_4.clicked.connect(self.dategen)

        self.ui.pushButton_5.clicked.connect(self.updateRecords)

        self.ui.pushButton_6.clicked.connect(self.displayRecordstoUpdate)
        self.ui.deleteButton.clicked.connect(self.deleteRecord)

        self.ui.comboBox.currentIndexChanged.connect(self.showRecords)

    def exit(self):
        sys.exit()
    def reset(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_8.clear()
        self.ui.lineEdit_9.clear()
        self.ui.lineEdit_10.clear()
        self.ui.lineEdit_11.clear()
    def dategen(self):
        self.date=self.ui.calendarWidget.selectedDate()
        self.ui.lineEdit_5.setText(self.date.toString("yyyy/MM/dd"))
    def register(self):
        id=self.ui.lineEdit.text()
        name=self.ui.lineEdit_2.text()
        code=self.ui.lineEdit_3.text()
        price=self.ui.lineEdit_4.text()
        doa=self.ui.lineEdit_5.text()
        mfg=self.ui.lineEdit_6.text()
        sname=self.ui.lineEdit_7.text()
        scontact=self.ui.lineEdit_8.text()
        saddr=self.ui.lineEdit_9.text()
        smname=self.ui.lineEdit_10.text()
        smcontact=self.ui.lineEdit_11.text()

        sql="insert into products(pid,prodName,prodCode,price,ArrivalDate,Manufacturer,SellerName,sellerNo,sellerAddress,SalesmanName,SalemanNo) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(id,name,code,price,doa,mfg,sname,scontact,saddr,smname,smcontact)
        cur.execute(sql,val)
        myconn.commit()
        QtWidgets.QMessageBox.about(self,"Success","Sucessfully Inserted")
        self.statusBar().showMessage('Sucessfully Inserted')
        self.reset()

    def showRecords(self):
        var=self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
        myconn=mysql.connector.connect(host="localhost", user="root",password="naveen",database="textile")
        cur = myconn.cursor()
        cur.execute("select * from products")
        res=cur.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for r_no, r_data in enumerate(res):
            self.ui.tableWidget.insertRow(r_no)
            for c_no, data in enumerate(r_data):
                self.ui.tableWidget.setItem(r_no,c_no,QtWidgets.QTableWidgetItem(str(data)))
        myconn.close()
        
    def displayRecordstoUpdate(self):
        myconn=mysql.connector.connect(host="localhost", user="root",password="naveen",database="textile")
        cur = myconn.cursor()
        self.prodid=self.ui.lineEdit.text()
        sql="select * from products where pid=%s"
        val=[(self.prodid)]
        cur.execute(sql,val)
        self.data=cur.fetchone()
        print(self.data)

        self.ui.lineEdit.setText(str(self.data[0]))
        self.ui.lineEdit_2.setText(str(self.data[1]))
        self.ui.lineEdit_3.setText(str(self.data[2]))
        self.ui.lineEdit_4.setText(str(self.data[3]))
        self.ui.lineEdit_6.setText(str(self.data[5]))
        self.ui.lineEdit_7.setText(str(self.data[6]))
        self.ui.lineEdit_8.setText(str(self.data[7]))
        self.ui.lineEdit_9.setText(str(self.data[8]))
        self.ui.lineEdit_10.setText(str(self.data[9]))
        self.ui.lineEdit_11.setText(str(self.data[10]))

        self.ui.lineEdit_5.setText(date.isoformat(self.data[4]))

    def updateRecords(self):
        id=self.ui.lineEdit.text()
        name=self.ui.lineEdit_2.text()
        code=self.ui.lineEdit_3.text()
        price=self.ui.lineEdit_4.text()
        doa=self.ui.lineEdit_5.text()
        mfg=self.ui.lineEdit_6.text()
        sname=self.ui.lineEdit_7.text()
        scontact=self.ui.lineEdit_8.text()
        saddr=self.ui.lineEdit_9.text()
        smname=self.ui.lineEdit_10.text()
        smcontact=self.ui.lineEdit_11.text()

        sql="update products set pid=%s,prodName=%s,prodCode=%s,price=%s,ArrivalDate=%s,Manufacturer=%s,SellerName=%s, sellerNo=%s,SellerAddress=%s, SalesmanName=%s,SalemanNo=%s where pid=%s"
        val=[id,name,code,price,doa,mfg,sname,scontact,saddr,smname,smcontact,id]
        cur.execute(sql,val)
        myconn.commit()
        self.statusBar().showMessage('Updated Successfully')
        self.reset()

    def deleteRecord(self):
        myconn=mysql.connector.connect(host="localhost", user="root",password="naveen",database="textile")
        cur = myconn.cursor()
        self.var=int(self.ui.lineEdit.text())
        sql="delete from products where pid=%s"
        val=[(self.var)]
        cur.execute(sql,val)
        myconn.commit()
        self.statusBar().showMessage('Deleted Successfully')


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    myconn = mysql.connector.connect(host = "localhost", user = "root",password = "naveen",database = "textile")  
    cur = myconn.cursor()
    w.show()
    sys.exit(app.exec_())
