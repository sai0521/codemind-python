n=int(input())
l=list(map(int,input().split()))
#print(l)
a,b=map(int,input().split())
#print(a,b)
fl=0
for i in range(a,b+1):
    if i in l:
        print(i)
        fl=1
        break
if fl==0:
    print(-1)