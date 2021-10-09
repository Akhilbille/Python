class Myclass:
    n=0
    def __init__(self):
        Myclass.n+=1
    @staticmethod
    def no_of_objects():
        print("No Of instances created : ",Myclass.n)
obj1=Myclass()
obj1=Myclass()
print(id(obj1),id(obj1))
Myclass.no_of_objects()

        
