#to find *no of characters,no of words,no lower case 
#chars,upper case,special chars,no of vowels and consonents
a=input("enter a  paragraph : ")
print(" no of chars  : ",len(a))
print(" no of words : ",len(a.split(" ")))
l,u,sp,v,con,v1,con1=0,0,0,"aeiou","bcdfghjklmnpqrstvwxyz",0,0
for i1 in a:
 if i1.islower():
  l=l+1
for i2 in a:
 if i2.isupper():
  u=u+1
for i3 in a:
 if i3.isalnum():
  pass
 else:
  sp=sp+1
for i4 in a:
 
 if i4.lower() in v:
  v1=v1+1
for i5 in a:
 
 if i5.lower() in con:
  con1=con1+1
print(" lower =%d \n upper=%d\n special chars : %d \n vowels =%d \n consonents =%d \n "%(l,u,sp,v1,con1))

