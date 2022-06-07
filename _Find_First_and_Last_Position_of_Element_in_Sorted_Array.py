n=int(input())
a=list(map(int,input().split()))
m=int(input())
c=0
for i in range(0,n):
    if a[i]==m:
        print(i,end=' ')
        c+=1
        x=i
if c==0:
    print('-1 -1')
if c==1:
    print(x,end=' ')