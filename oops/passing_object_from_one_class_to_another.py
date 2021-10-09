class Company_Personal:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def details(self):
        print(f"Mr.{self.name}")
        print(f"Your age is {self.age}")
        print(f"Your salary is {self.salary}")


class Salary_Increment:
    @staticmethod
    def increment(obj):
        obj.salary += 10000
        obj.details()


kiran = Company_Personal("Kiran", 21, 100000000)
Salary_Increment.increment(kiran)
Salary_Increment.increment(kiran)
