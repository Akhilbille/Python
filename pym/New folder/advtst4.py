try: 
 l=[]
 for i in range(10000):
  i=(input("enter a num or done to exit program : "))
  if(i!="done"):
   l.append(int(i))
  elif(i=="done"):
   break
except ValueError:
 print("enter only integers")  
print("maximum number is :",max(l))
print("minimum number is  :",min(l))