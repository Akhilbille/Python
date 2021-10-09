class Mobile:
    def __init__(self,name_of_brand,ram,initial_cost):
        self.brand=name_of_brand
        self.ram=ram
        self.__price=initial_cost
    def set_price(self,cost):
        self.__price=cost
    def get_price(self):
        return(self.__price)
    def discount(self,num):
        self.num=num
        self.amount=self.get_price()
        self.final_disc=(self.num/100)*self.amount
        self.final_price=(self.amount-self.final_disc)
        return(self.final_price)
    def buy(self):
        return("Thank you for shopping in our stores... Visit Again")

mob1=Mobile("MI",16,20000)
mob1.set_price(22000)
print(mob1.get_price())
final_price=mob1.discount(int(input("Enter discount percentage : ")))
print('Final price is :',final_price)
print(mob1.buy())
