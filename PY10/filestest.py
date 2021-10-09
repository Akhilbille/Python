no_of_strings=int(input('Enter No of Strings: '))
f=open('TextFile.txt','a')
for i in range(no_of_strings):
    f.write(input('Enter a String: ')+'\n')
f.close()
