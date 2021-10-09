n=int(input("Enter a num : "))
if 1<=n<=100:
    if(n%2!=0) or (6<=n<=20) and (n%2==0):
        print("Weird")
    elif (n%2==0) and (2<=n<=5) or (n%2==0) and (n>20):
        print("NOt weird")
else:
    print("Enter input with in 1 to 100")
     
