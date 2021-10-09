str=input("Enter a string  :")
unique_str=set(str)
l=[]
for i in unique_str:
    print(f"{i}={str.count(i)}",end=" ")
    l.append(str.count(i))
print(f"\nsum of all count values : {sum(l)}")
