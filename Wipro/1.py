n = int(input())
den = int(input())
arr = [int(i) for i in input().split()]
res = 0
for i in arr:
    res+=(i//den)
print(res)

