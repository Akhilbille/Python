str=input()
str1=set(str)
str1=("".join(str1))
str1=sorted(str1)



for i in str1:
    print("{}{}".format(i,str.count(i)),end="")
    #print(f'{i}{str.count(i)}',end='')
    
    
