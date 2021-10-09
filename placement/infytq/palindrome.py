lst1=[]
lst2=[]
def palin(inum):
    for i in range(innum):
        temp=str(i)
        if (temp==(str(i))[::-1]):
            lst1.append(temp)
        num1=lst1[0]
    count=inum+1
    for j in range(inum,count):
        if (temp==(str(j))[::-1]):
            num2=temp
            break
        count+=1
    pal=num1+num2
    if (pal==pal[::-1]):
        print(pal)
    else:
        palin(inum=inum-1)
innum=int(input("enter num : "))
palin(innum)
 
        
