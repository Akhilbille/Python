class Father:
    def __init__(self):
        self.money = 1000000000000

    def buy_bike(self, cost):
        self.cost = cost
        if self.money > self.cost:
            print("yes We can purchase bike")
        else:
            print("No my son no sufficient money,We will try next time")


class Son(Father):
    def __init__(self):
        self.money = 1000000000000

    def buy_bike(self, cost):
        self.cost = cost
        print("Yes I can buy a bike by myself")


kiran = Son()
kiran.buy_bike(100000000)
