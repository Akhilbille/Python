a=int(input("enter a starting number of range : "))
b=int(input("enter a ending number of range : "))
k=int(input("enter a number to consider last k values :"))
l=[]
for i in range(b,a-1,-1):
 if i%2==0:
  l.append(i)
print("output : ",sum(l[:k]))
 
