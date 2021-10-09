class Person:
    name : str
    age : int

    def details(self):
        print('Name : ',self.name)
        print('Age  :',self.age)

akhil = Person()
akhil.name = "AKhil"
akhil.age = 21
akhil.details()

kiran = Person()
kiran.name = 'kiran'
kiran.age = 21
kiran.details()
