sum=0
num=int(input("Enter a number :"))
res=(num*(num+1))/2
print(f"Sum of {num} natural numbers is {res}")
print(f"Sum of first {num} odd numbers is  {num**2}")

print(f"Sum of first {num} even numbers is  {num*(num+1)}")

for i in range(1,num+1):
    sum=sum+i
print(sum)
    
