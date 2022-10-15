n=int(input())
l=list(map(int,input().split()))
m=l[::-1]
fl=0
a,b=map(int,input().split())
for i in range(b,a-1,-1):
    if i in m:
        print(i)
        fl=1
        break
if fl==0:
    print(-1)