f=open("data.txt","r")
words=characters=lines=cap=low=digits=spclchars=0
for l in f:
    lines+=1
    words=len(l.split())
    characters=len(l)
    for il in l:
        if il.isalpha():
            if il.isupper():
                cap+=1
            else:
                low+=1
        elif il.isdigit():
            digits+=1
        else:
            spclchars+=1
print("No of lines in text : ",lines)
print("No of words in text : ",words)
print("No of characters in text : ",characters)        
print("No of upper case letters in text : ",cap)
print("No of lower case letters in text : ",low)
print("No of digits in text : ",digits)
print("No of special characters in text : ",spclchars)
f.close()
