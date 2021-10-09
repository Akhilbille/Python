class Student:
    counter=0
    
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
    @classmethod
    def modify_class(cls):
        cls.counter+=1
        return cls.counter
    def modify_self(self):
        self.counter+=1
        return self.counter
    
    
s1=Student("akhil","ECE")
print(Student.counter)
print(s1.counter)

(s1.modify_class())
print(s1.counter)
print(Student.counter)


print(self.counter)

