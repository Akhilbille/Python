s=input()
if s[0].isalpha():
 print("if the string starts with character")
 for i in range(0,(len(s)-1),2):
  print(s[i]*int(s[i+1]),end="")
else:
 print("if the string starts with number")
 for i in range(0,(len(s)-1),2):
  print(s[i+1]*int(s[i]),end="")