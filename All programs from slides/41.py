from math import *
def strong_number(num):
    sum=0
    for i in num:
        sum=sum+factorial(int(i))
    if sum==int(num):
        return(True)
    else:
        return(False)
    
ans=strong_number(input('enter a number:'))
print(ans)

