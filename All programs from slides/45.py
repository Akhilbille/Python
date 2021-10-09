def modify(local):
    local+=12
    global num
    num+=12
    print(num)
    #print(f"local value is {local}")
num=25
modify(num)
#print(f"global value{num}")
#print(local)
print(num)
