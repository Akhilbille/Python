n = int(input())
arr = [int(i) for i in input().split()]
res = (sorted(arr))[::-1]

l1 = res[:(n//2)]
l2 = (res[(n//2):])[::-1]
print(l1)
for i in range(0,n//2):
    print(l1[i],l2[i])
 
