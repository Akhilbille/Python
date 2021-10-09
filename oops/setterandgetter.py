import sys


class Bank:
    def __init__(self, name, account_num, password, balance):
        self.name = name
        self.account_num = account_num
        self.password = password
        self.__balance = balance

    def getbalance(self):
        return self.__balance

    def details(self):
        print(f"Hii Mr.{self.name} Welcome back Singapore Bank")
        print(f"Your account number is {self.account_num}")


kiran = Bank("kiran", 10102500, 123456, 1000000000)
choice = input("Do you want to access your details y/n ")
if choice.lower() == "y":
    kiran.details()
    choice = input("Do you want to check your balance y/n")
    if choice.lower() == "y":

        password = int(input("Enter your password  : "))
        if password == kiran.password:
            print(f"Your balance is : {kiran.getbalance()}")
        else:
            print("Wrong password")
            sys.exit()
    else:
        print("Thank you Visit Again")
else:
    print("Thank you!")
