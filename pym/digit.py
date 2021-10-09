l=[]
n=(input("enter a number : "))
m=int(n)
for i in range(len(n)):
 l.append(m%10)
 m=m//10
print("total number of digits : ",len(l))
print("sum of the individual nums : ",sum(l)) 
