class Classvariable:
    c = 2

    @classmethod
    def modify(cls):
        cls.c += 1

    def __init__(self, c1):
        self.c1 = c1

    def modify_c1(self):
        self.c1 += 1


s1 = Classvariable(1)
s2 = Classvariable(1)
print(s1.c)
print(s1.c1)
print(s2.c1)
s1.modify()
print(s1.c)
print(s1.c1)
print(s2.c1)
s1.modify_c1()

print(s1.c)
print(s1.c1)
print(s2.c1)
s1.modify_c1()
s2.modify_c1()
print(s1.c)
print(s1.c1)
print(s2.c1)
