num=int(input("enter a number to find a palindrome : "))
temp=num
reverse=0
while num>0:
    rem=num%10
    
    reverse=reverse*10+rem
    num=num//10
    
if temp == reverse:
    print("Its a palindrome")
else:
    print("It's not a palindrome")
print(reverse)
print(temp)
