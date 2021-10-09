s=input("enter a string : ")#10
sub=input("enter a sub string to join :")
l1,l2=len(s),len(sub)
n=int(input("enter a place value to join substring : "))
n=n-1
l=[]
for i in range(n):#0,1,2,3,4,5
 l.append(s[i])
for j in range(l2):#0,1,2,3,4
 l.append(sub[j])
for k in range(n,l1):
 l.append(s[k])
print("".join(l))
