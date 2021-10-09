class Names:
    def __init__(self,n=" ",b=" ",y=0):
        self.name=n
        self.branch=b
        self.year=y
        self.talk()
    def talk(self):
        print("Hii..My self %s"%(self.name))
        print("I am from %s"%(self.branch))
        print("Now I am in %d year"%(self.year))

p1=Names()
