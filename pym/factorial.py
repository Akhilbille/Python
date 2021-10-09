def factorial(n):
    temp=1
    for i in range(1,n+1):
        temp=temp*i
    print("Factorial of %d ! =  %d "%(n,temp))
factorial(int(input("enter a number = ")))
