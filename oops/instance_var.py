class Hello:
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def modify_a1(self):
        self.a1 += 1

    def modify_a2(self):
        self.a2 += 1


obj1 = Hello(1, 2)
print(obj1.a1)
print(obj1.a2)
obj1.modify_a1()
print(obj1.a1)
obj1.modify_a1()
obj1.modify_a2()
print(obj1.a2)
print(obj1.a1)
