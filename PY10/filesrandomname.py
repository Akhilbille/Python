from random import *
f=open('names.txt','r')
l=[]
for i in f:
    l.append(i.strip('\n'))

print(choice(l))
