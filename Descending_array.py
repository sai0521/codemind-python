n=int(input())
l=list(map(int,input().split()))
m=l
m=sorted(m,reverse=True)
if l==m:
    print("yes")
else:
    print("no")
