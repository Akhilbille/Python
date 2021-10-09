#Naveen Kumar@7852 -Chars-17, W2,UA-2,LA-9,D-4,Sc-1,sp-1
s=input('Enter a String:')
chars=len(s)
words=len(s.split())
ua=la=d=sc=sp=0

for i in s:#Naveen Kumar@7852
    if i.isalpha():
        if i.isupper():
            ua+=1
        elif i.islower():
            la+=1
    elif i.isdigit():
        d+=1
    elif i.isspace():
        sp+=1
    else:
        sc+=1

print('No of Characters: ',chars)
print('No of Words: ',words)
print('No of Uppercase Alphabets: ',ua)
print('No of Lowercase Alphabets: ',la)
print('No of Digits: ',d)
print('No of Spaces: ',sp)
print('No of Special Characters: ',sc)
        
