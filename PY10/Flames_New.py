





n1=(input("Enter First person Name: ").lower()).replace(" ","")
n2=(input("Enter Second person Name: ").lower()).replace(" ","")
print(n1)
print(n2)
flames=['Friendship','Love','Affection','Marriage','Enemy','Siblings']
for i in n1:#viratkohli
   for j in n2: #anushkasharma
      if i==j:
           n1=n1.replace(i,'',1)
           n2=n2.replace(j,'',1)
           break
count=len(n1+n2)
print("Count : ",count)
if count>0:
   while len(flames)>1:
        c=count%len(flames)
        index=c-1
        if index>=0:
           left=flames[:index]
           right=flames[index+1:]
           flames=right+left
        else:
            flames=flames[:len(flames) - 1]
   print("Relationship is :",flames[0])
else:
   print("FLAMES can't be checked for same Names")


