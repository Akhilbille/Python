class Father:
    def __init__(self, fathermoney):
        self.fathermoney = fathermoney

    def buy_bike(self, cost):
        self.cost = cost
        if self.money > self.cost:
            print("yes We can purchase bike")
        else:
            print("No my son no sufficient money,We will try next time")


class Son(Father):
    def __init__(self, sonmoney, fathermoney):
        super().__init__(fathermoney)
        self.money = sonmoney

    def buy_bike(self, cost):
        self.cost = cost
        if self.cost <= self.money:
            print("Yes I can buy a bike by myself")
        elif self.cost <= self.fathermoney + self.money:
            print("My Son I can Help you")
        else:
            print("We can try next year")


kiran = Son(int(input("Enter son money  :")), int(input("Enter father money  :")))
kiran.buy_bike(int(input("Enter bike cost : ")))
