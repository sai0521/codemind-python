a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
c=0
l1=set(x)
l2=set(y)
for i in l1:
    if i not in l2:
        c+=1
for i in l2:
    if i not in l1:
        c+=1
print(c)