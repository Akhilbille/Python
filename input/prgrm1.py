for i in range(10):
    if i==11:
        print(i)
        break
else:
    print("i am else")


var="we love {}"
print(var.format("dba"))
name="akhil"
print("%-20s)"%name)
num=2.01233
print("%.2f"%num)
n1=12
print("number1 : {0} name={1}".format(n1,name))
data=[x for x in input("Enter data seperated by comma : ").split(",")]
for words in data:
    print(words)
data1,data2=[x for x in input("Enter data seperated by comma : ").split(",")]
print(data1,data2)


