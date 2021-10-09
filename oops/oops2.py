class Names:
    def __init__(self):
        self.name="SAI"
        self.branch="ECE"
        self.year="2 year"
    def talk(self):
        print("Hii..My self %s"%(self.name))
        print("I am from %s"%(self.branch))
        print("Now I am in %s"%(self.year))

p1=Names()
print(p1.branch)
p1.talk()
print("_______________________________________________________________")
#creating a  new object and modifying data
p2=Names()
p2.name="jogi sai"
p2.branch="Ece"
p2.year="3 year"
p2.talk()



        
