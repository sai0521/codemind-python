n=int(input())
l=list(map(int,input().split()))
m=(n//2)
a=0
b=0
for i in range(0,m):
    a+=l[i]
for i in range(m,n):
    b+=l[i]
print(abs(a-b))