N = int(input())
sales_ID=[x for x in input().split()]
lp_Id=['a','e','i','o','u','A','E','I','O','U']
tc=len(sales_ID)
count=0
if 0<=N<=10**6:
    for i in sales_ID:
        if i in lp_Id:
            count+=1

print(tc-count)
