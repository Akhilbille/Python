class Teacher:
    def setId(self, Id):
        self.Id = Id

    def getId(self):
        return self.Id

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

    def setaddress(self, address):
        self.address = address

    def getaddress(self):
        return self.address

    def setsalary(self, salary):
        self.salary = salary

    def getsalary(self):
        return self.salary

    def details(self):
        print(self.getId())
        print(self.getname())
        print(self.getaddress())
        print(self.getsalary())
        
