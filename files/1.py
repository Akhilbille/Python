f=open('data1.txt','r+')
string=input('enter a string:')
f.write(string)
str=f.read()
for i in str:
    print(i)
f.close()


