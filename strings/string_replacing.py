string=input("Enter a string : ")
sub=input("Enter a sub string : ")
n=int(input("Enter index value : "))
n-=1
new_str=[]
for i in range(0,n):
    new_str.append(string[i])
for i in range(len(sub)):
    new_str.append(sub[i])
for i in range(n,len(string)):
    new_str.append(string[i])
replaced_value="".join(new_str)

print(replaced_value)