start=int(input("Enter a number to start : "))
end=int(input("Enter a number to end : "))
for i in range(start,end+1):
    print(f"bin({i}) = {bin(i)}   oct({i}) = {oct(i)}   hex({i}) = {hex(i)}") 
