n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
fl=0
for i in range(b,a-1,-1):
    if i in l:
        print(i)
        fl=1
        break
if fl==0:
    print(-1)