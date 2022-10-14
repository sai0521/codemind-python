n=int(input())
m=int(input())
s=0
for i in range(n):
    l1=list(map(int,input().split()))
    s+=sum(l1)
print(s)