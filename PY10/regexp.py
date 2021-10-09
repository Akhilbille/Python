



import re
s=input("Enter Mobile Number:")

m=re.fullmatch("(0|91|\+91)?[6-9][0-9]{9}",s)

if m!=None:
   print("Valid Mobile Number");
else:
   print("Invalid Mobile Number")
