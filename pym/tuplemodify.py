t=tuple([int(x) for x in input().split()])
sub=tuple([int(i) for i in input().split()])
pl=int(input("enter data by seperating by spaces : "))
n=t[:pl-1]
n1=n+sub
n=n1+t[pl-1:]
print(n)