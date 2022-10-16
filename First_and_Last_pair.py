n=int(input())
l=list(map(int,input().split()))
m=l[::-1]
c=[]
fl=0
if n%2==0:
    x=n//2
else:
    x=(n//2)+1
    fl=1
k=1
t=0
while t!=x:
    l.insert(k,m[t])
    l.pop(-1)
    k+=2
    t+=1
if fl==1:
    l.append(0)
print(*l)
    