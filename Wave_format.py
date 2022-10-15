n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
k=0
if n%2!=0:
    n-=1
while 1:
    if k==n:
        break
    x=a[k]
    y=a[k+1]
    temp=x
    a[k]=y
    a[k+1]=temp
    k+=2
print(*a)