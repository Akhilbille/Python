#Reverse a number
num=int(input("Enter a number  : "))
while num>0:
    rem=num%10
    print(rem,end="")
    num//=10
