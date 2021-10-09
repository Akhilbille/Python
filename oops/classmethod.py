class classmethod:
    glo=20
    @classmethod
    def __init__(cls):
        cls.x=10
    def modify(cls):
        obj.glo+=1
        cls.x+=1
    def output(cls):
        print("Th global value is ",cls.glo)
        print("The global value using object value is ", obj.glo)
        print("The X value is ",cls.x)
        
obj=classmethod()
obj.modify()
obj.output()
obj2=classmethod()
obj2.output()