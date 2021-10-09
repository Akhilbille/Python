s=input().upper()
l=[]
for k in s:
 if k not in l:
  print("%d%s"%(s.count(k),k),end="")
  l.append(k)
        

        
   
