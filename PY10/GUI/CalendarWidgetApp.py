import sys

from PyQt5.QtWidgets import QMainWindow,QApplication
from CalendarWidgetUi import *

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.displayDate)
        self.ui.comboBox.currentIndexChanged.connect(self.cbox)
    def displayDate(self):
        self.date=self.ui.calendarWidget.selectedDate()
        self.ui.lineEdit.setText(self.date.toString("yyyy/MM/dd"))
        self.ui.label.setText(self.date.toString("yyyy/MM/dd"))
    def cbox(self):
        self.val=self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
        self.ui.lineEdit_2.setText(self.val)

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    f=open('text_file.txt','a+')
    w.show()
    sys.exit(app.exec_())
