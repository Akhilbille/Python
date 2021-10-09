# Greatest among three numbers
a=int(input("Enter a number : "))
b=int(input("Enter b number : "))
c=int(input("Enter c number : "))
if (a>b):
    if a>c:
        print("A is big")
    else:
        print("c is big")
elif (b>c):
    print("b is big")
else:
    print("c is big")


