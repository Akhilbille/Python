class Father:
    def __init__(self,prop=0):
        self.prop=prop
    def dis_prop(self):
        print("Father's prop : ",self.prop)
class Son(Father):
    def __init__(self,prop1=0,prop=0):
        super().__init__(prop)
        self.prop1=prop1
    def display_prop(self):
        print("Total prop of child : ",self.prop1+self.prop)

s=Son(200.00,800.00)
s.display_prop()
