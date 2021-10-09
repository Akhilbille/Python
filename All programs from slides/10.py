num1=int(input("enter a number  : "))
num2=int(input("enter a number  : "))
if num1>num2:
    print(f"{num1} is BIG ")
else:
    print(f"{num2} is BIG")

print(f"{num1} is BIG ") if num1>num2 else print(f"{num2} is BIG ")

