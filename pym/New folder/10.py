n=int(input())
s1={int(i) for i in input().split()}
m=int(input())
s2={int(j) for j in input().split()}
print(s1.symmetric_difference(s2))