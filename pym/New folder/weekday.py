m={0:january,3:febrauary,3:march,6:april,1:may,4:june,6:july,2:august,5:september,0:october,3:november,5:december}
code={1500:0,1600:6,1700:4,1800:2,1900:0,2000:6,2100:4,2200:2}
w={0:sunday,1:monday,2:tuesday,3:wednesday,4:thursday,5:friday,6:saturday}
d,m,y=[int(x) for x in input("enter date in format dd/mm/yyyy").split("/")]
c=code[y-(y%100)]
year=y%100
leap=y//4
month=m[m]
tot=c+year+leap+month+d
print(w[tot%7])