string=input("Enter a string : ")
sub=input("Enter a sub string to search : ")
for i in string:
    if sub==i:
        print("String '{}' found at {}".format(sub,string.find(sub)))
        
        break
else:
    print("string not found")
