n=int(input())
i=int(input())
x=int(input())
y=int(input())
lst=[]
lst2=[]
for m in range(8):
    for n in range(8,0,-1):
        a=m*x+n*y
        if a==n:
            lst.append(m)
            lst2.append(n)
        if m==n:
            print(m)
print(lst)
print(lst2)