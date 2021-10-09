from teacher import Teacher


class Student(Teacher):
    def setmarks(self, marks):
        self.marks = marks

    def getmarks(self):
        return self.marks

    def details(self):
        print(self.getId())
        print(self.getname())
        print(self.getaddress())
        print(self.getmarks())


naveen = Teacher()
naveen.setId(1)
naveen.setname("Naveen")
naveen.setaddress("Venugopal Nagar")
naveen.setsalary("100000000000000")
naveen.details()
print("================================================")

kiran = Student()
kiran.setId(1)
kiran.setname("Kiran")
kiran.setaddress("Syndicate nagar")
kiran.setmarks("100")
kiran.details()
