a=input("enter a name : ").lower()
b=input("enter another name : ").lower()
n=int(input("enter a number to compare : "))
if(len(a)==len(b)):
 if(a[n]==b[n]):
  print("yes")
 else:
  print("no")
else:
 print(" length of strings are not matched ,enter equal length of strings")