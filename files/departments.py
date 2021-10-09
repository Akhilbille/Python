
with open("datas.txt", "r+") as f:
    str = f.readlines()
    l = []
    for i in str:

        l.append((i.replace("\n", "")).title())

print(l)   
print(len(l))