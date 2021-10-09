#getting string and converting into dictionary
string="a=1,b=2,c=3"
l=[]
for value in string.split(","):
    l.append(value.split("="))
d=dict(l)
print(d)
for i,j in d.items():
    d[i]=int(j)

print(d)
