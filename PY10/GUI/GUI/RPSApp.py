import sys
from random import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from RPSUi import *

class RPSGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)       
        self.ui.pushButton.clicked.connect(self.rock)
        self.ui.pushButton_2.clicked.connect(self.paper)
        self.ui.pushButton_3.clicked.connect(self.scissor)
        self.show()
    def rock(self):
        global user_choice
        global comp_choice
        user_choice='rock'
        comp_choice=choice(['rock','paper','scissor'])
        print(user_choice,comp_choice)
        answer=result(user_choice,comp_choice)
        self.ui.textEdit.setText(answer)
    def paper(self):
        global user_choice
        global comp_choice
        user_choice='paper'
        comp_choice=choice(['rock','paper','scissor'])
        answer=result(user_choice,comp_choice)
        self.ui.textEdit.setText(answer)
    def scissor(self):
        global user_choice
        global comp_choice
        user_choice='scissor'
        comp_choice=choice(['rock','paper','scissor'])
        answer=result(user_choice,comp_choice)
        self.ui.textEdit.setText(answer)
def result(human_choice,comp_choice):
        global player_win
        global computer_win
        global tie
        if user_choice==comp_choice:
            print("Tie")
            tie+=1
        elif((comp_choice=="rock" and user_choice=="scissor")or(comp_choice=="scissor" and user_choice=="paper")or(comp_choice=="paper" and user_choice=="rock")):
            print("Computer wins")
            computer_win+=1
        else:
            print("Player wins")
            player_win+=1
        answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n   Your Score : {u} \n   Computer Score : {c} \n   Matches in Tie : {t} ".format(uc=user_choice,cc=comp_choice,u=player_win,c=computer_win,t=tie)
        return answer


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = RPSGame()
    player_win = computer_win = tie=0
    user_choice = comp_choice = "" 
    w.show()
    sys.exit(app.exec_())
