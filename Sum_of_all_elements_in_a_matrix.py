n,m=map(int,input().split())
b=[]
for i in range(0,n):
    a=list(map(int,input().split()))
    b.append(a)
c=[]
s=0
for i in range(0,n):
    for j in range(0,m):
        s+=b[i][j]
    
print(s)