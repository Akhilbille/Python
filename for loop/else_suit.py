l=[1,2,3,4,5]
value=int(input("Enter a number to search in a list : "))
for i in l:
    if i == value:
        print("We found it")
        break
else:
    print("sorry we not found it")