class Student:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


i = 0
stu = int(input("Enter number of students :  "))
while i < stu:
    s1 = Student()
    name = input("Enter a name : ")
    s1.set_name(name)
    print(s1.get_name())
    i += 1
