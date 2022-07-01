n,m=map(int,input().split())
b=[]
for i in range(0,n):
    a=list(map(int,input().split()))
    b.append(a)
s=0
for i in range(1,n-1):
    for j in range(1,m-1):
        s+=b[i][j]
print(s)