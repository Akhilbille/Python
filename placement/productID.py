def cal(productID):
    count=0
    for i in productID:
        if i not in ["a","e","i","o","u","A","E","I","O","U"]:
            count+=1
    return count


            

def fb(flowerStick, random):
    li=[]
    li1=[]
    li2=[]
    for i in range(random):
        li.append(flowerStick[i])
    li1=sorted(li)
    
    print(li1)
    for j in range(random,len(flowerStick)):
        li2.append(flowerStick[j])
    li2=sorted(li2,reverse=True)
    return(li1+li2)

    
print(fb([11,7,5,10,46,23,16,8],3))
print(cal(["a","v","i","k","e","l"]))
