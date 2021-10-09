
def var_len(a,*b):
    sum=0
    print(type(b))
   
    for i in b:
        sum=sum+i
    print(a+sum)

var_len(1,2,3,4,5,6)
