n1=int(input('enter n1 value:'))
n2=int(input('enter n2 value:'))
count=0
for i in range(n1,n2+1):
    str_num=str(i) 
    for j in len(str_num):
        if i.count(j)==2:
            break
    else:
        count+=1

print(count)