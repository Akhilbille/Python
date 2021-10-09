#Swapping numbers
a=int(input("enter a number : "))
b=int(input("enter a number : "))
print(f"Before swapping two nums {a},{b}")
temp=a
a=b
b=temp
print(f"After swapping two nums {a},{b}")

# Swapping With out using temp variable
num1=int(input("enter a number : "))
num2=int(input("enter a number : "))
print(f"Before swapping two nums {num1},{num2}")
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(f"After swapping two nums {num1},{num2}")


