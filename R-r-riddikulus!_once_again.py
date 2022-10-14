n,m=map(int,input().split())
l1=list(map(int,input().split()))
while m:
    x=l1[0]
    l1.pop(l1.index(x))
    l1.insert(n-1,x)
    m-=1
print(*l1)