n=int(input("enter a range of the dict : "))
d={}
print(d)
for i in range(n):
 k=input("enter key value : ")
 v=input(" enter a value for pairing  : ")
 d.update({k:v})
print(d)