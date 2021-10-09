def modify(lst):
    lst.append(12)
    print(lst)
    print(id(lst))
lst=[1,2,34,6]
modify(lst)
print(lst,id(lst))
