from math import *
num=fabs(int(input('Enter a Number: ')))
count=0
while num>0:
    num=num//10
    count+=1

print('No of Digits: ',count) 
