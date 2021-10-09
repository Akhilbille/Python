num1=int(input("Enter a number : "))
num2=int(input("Enter a number : "))
num3=int(input("Enter a number : "))
if num1 > num2:
    if num1>num3:
        print(f"{num1} is BIG")
    else:
        print(f"{num3} is BIG")
if num2>num3:
    print(f"{num2} is BIG")
else:
    print(f"{num3} is BIG")
