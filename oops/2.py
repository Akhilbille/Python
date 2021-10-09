class Abstract:
    
    def __init__(self):
        self.__private = 100

    def set_private(self,newnum):
        self.__private=newnum

    def get_private(self):
        return self.__private


obj = Abstract()
print(obj.get_private())
print(obj._Abstract__private)
obj.set_private(1000)
print(obj._Abstract__private)
