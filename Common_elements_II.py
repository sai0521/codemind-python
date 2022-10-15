a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
c=[]
l1=[]
l2=[]
for i in x:
    if i not in l1:
        l1.append(i)
for i in y:
    if i not in l2:
        l2.append(i)
for i in l1:
    if i not in l2:
        c.append(i)
for i in l2:
    if i not in l1:
        c.append(i)
print(*c)