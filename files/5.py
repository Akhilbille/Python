f = open("data.txt", "a+")
while str != "@":
    str = input()
    if str != "@":
        f.write(str + "\t")
f.seek(0, 0)
str = f.read()
print(str)
