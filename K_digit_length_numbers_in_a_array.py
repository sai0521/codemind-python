def count(x):
    c=0
    if x<0:
        x=-(x)
    if x==0:
        return 1
    while x:
        x=x//10
        c+=1
    return c

n,m=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    if m==count(i):
        c+=1
print(c)