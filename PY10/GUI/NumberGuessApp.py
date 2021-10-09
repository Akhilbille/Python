import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from NumberGuessUi import *
from random import *

class NumberGuess(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)       

        self.ui.Check.clicked.connect(self.GameCode)
        self.ui.Reset.clicked.connect(self.ResetCode)
        self.show()
        
    def ResetCode(self):
        self.ui.TextField.setText('')
    def GameCode(self):
        self.secnum=randint(1,50)
        self.count=0
        for i in range(5):
           self.count+=1
           self.guess = int(self.ui.TextField.text())
           if self.guess>self.secnum:
               self.ui.OutputLabel.setText('Your Guess is High')
           elif self.guess<self.secnum:
               self.ui.OutputLabel.setText('Your Guess is Low')
           else:
               break
        if self.guess==self.secnum:
            QtWidgets.QMessageBox.about(self,"Congrats","Congratulations...! You have Guessed the Number :-)in %d chances" %self.count)
            
        else:
            QtWidgets.QMessageBox.about(self,"Sorry",'Better Luck Next Time :-(. Secret Number is %d' %self.secnum)
             
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = NumberGuess()
    w.show()
    sys.exit(app.exec_())
