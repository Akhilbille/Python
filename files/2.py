f=open('data.txt','a+')
print('enter some data at the end enter @')
while str!='@':
    str=input()
    if str!='@':
        f.write(str+'\t')
f.close()    