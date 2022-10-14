n,m=map(int,input().split())
l1=list(map(int,input().split()))
x=c=0
for i in l1:
    if i>m:
        c+=1
    else:
        x+=1
    if c==2:
        break
print(x)