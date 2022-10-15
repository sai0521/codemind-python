n=int(input())
l=list(map(int,input().split()))
m=sorted(l,reverse=True)
if l==m:
    print("yes")
else:
    print("no")