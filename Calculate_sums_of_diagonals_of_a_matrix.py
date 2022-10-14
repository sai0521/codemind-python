n=int(input())
m=[]
for i in range(n):
    l=list(map(int,input().split()))
    m.append(l)
s=0
p=0
for i in range(n):
    for j in range(n):
        if i==j:
            s+=m[i][j]
        if i+j==n-1:
            p+=m[i][j]
print("Principal Diagonal:"+str(s))
print("Secondary Diagonal:"+str(p))