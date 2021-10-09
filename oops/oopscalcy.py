class calculator:
    def __init__(self,a=0,b=0):
        self.num1=a
        self.num2=b
    def addition(self):
        print("Sum is ",self.num1+self.num2)
    def Subtraction(self):
        print("Subtraction is ",self.num1-self.num2)

pb1=calculator(a=int(input("Enter a number : ")),b=int(input("Enter b number :" )))
process=input("Tell me Either you need to perform addition or subtraction :")
pb1.addition() if(process=="addition") else pb1.subtraction()
