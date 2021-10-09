n1=int(input("enter a number "))
n2=int(input("enter a number "))
n3=int(input("enter a number "))
if n1<n2:
    if n1<n3:
        print(n1,"is small")
    else:
        print(n3,"is small")
elif n2<n3:
    print(n2,"is small")
else:
    print(n3,"is small")
    
