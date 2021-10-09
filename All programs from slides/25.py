#Number of digits in a number
num=int(input("ENter a number : "))
count=0
while num>0:
    
    count+=1
    num//=10
print(count)

#Number of digits of a number using type casting
num=int(input("Enter a number : "))
num= str(num)
print(f"Number ofdigits in a number{num} are {len(num)}")
