# Abstraction
class Bank:
    def __init__(self,name,account):
        self.name = name
        self.__accountnumber = account 

    def __str__(self):
        return(self.name)

kiran = Bank("Kiran","123456")


print(kiran.name)
print(kiran)
print(kiran._Bank__accountnumber)