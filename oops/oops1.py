class Flower:
    name="rose"
    color="red"
    def describe(cls):
        print("Rose is a very beaultiful flower")

obj1=Flower()
obj1.describe()

print(obj1.name)
print(obj1.color)

obj2=Flower()
obj2.name="hibiscus"
obj2.color="light_red"
print(obj2.name)
print(obj1.name)
print(obj2.color)

    
    
