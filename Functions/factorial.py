

def fact(num):
    res=1
    for i in range(num,0,-1):
        res=res*i
    print("%d : %d "%(num,res))
for i in range(int(input("Enter initial num : ")),int(input("Enter final num : "))):
    fact(i)
