n,m=map(int,input().split())
b=[]
for i in range(0,n):
    a=list(map(int,input().split()))
    b.append(a)
c=[]
for i in range(0,m):
    s=0
    for j in range(0,n):
        s+=b[j][i]
    c.append(s)
print(*c)