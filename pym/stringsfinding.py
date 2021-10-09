paragraph=input("Enter a pragraph : ")
lw=up=dg=sp=0
for char in paragraph:
    if(char.isalnum()):
        if (char.isupper()):
            up+=1
        elif (char.islower()):
            lw+=1
        else:
            dg+=1
    else:
        sp+=1
print("TOtal Number of upper case letters are : ",up)
print("TOtal Number of  lower letters are : ",lw)
print("TOtal Number of  digits are : ",dg)
print("TOtal Number of special characters  are : ",sp)
