import re
import keyword as k
var=input("enter a variable : ")
r=re.fullmatch("[a-zA-Z_][\w_]*",var)
if r!=None and (var not in k.kwlist):
 print("valid variable")
else:
 print("not a valid variable")