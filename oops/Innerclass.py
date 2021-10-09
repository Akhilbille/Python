class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Hii Mr {self.name} \nYour age is {self.age}")

    class Dob:
        def __init__(self, dob):
            self.dob = dob

        def details(self):
            print(f"You born on {self.dob}")


kiran = Person("kiran", 21)
kiran.details()
kiran = Person("kiran", 21).Dob("13-03-2000")
kiran.details()
