n=int(input())
l=list(map(int,input().split()))
fl=0
s=0
a,b=map(int,input().split())
for i in range(a,b+1):
    if i in l:
        s+=i
        fl=1
if fl==0:
    print(-1)
else:
    print(s)