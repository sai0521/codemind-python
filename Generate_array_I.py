n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(0,n,2):
    k=l[i+1]
    while k:
        s.append(l[i])
        k-=1
print(*s)