list=[]
x=1
while  x<=10:
    num=int(input("Enter a number : "))
    list.append(x)
    x+=1
sum=sum(list)
print(f"Average is {sum/len(list)}")
