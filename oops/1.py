class Flower:
    def __init__(self, name, colour, fragrance):
        self.name = name
        self.colour = colour
        self.fragrance = fragrance
        self.features()

    def features(self):
        print(f"I am {self.name} flower")
        print(f"I am in {self.colour} colour")
        print(f"My fragrance is {self.fragrance} flower")


f1 = Flower(
    input("Enter flower name :"),
    input("Enter flower colour :"),
    input("Ener flower fragrance :"),
)
f2 = Flower(
    input("Enter flower name :"),
    input("Enter flower colour :"),
    input("Enter flower fragrance :"),
)
print(id(f1))
print(id(f2))
