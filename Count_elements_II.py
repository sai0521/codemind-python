n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=set(a)
b=set(b)
x=list(a)
y=list(b)
c=0
for i in x:
    if i not in y:
        c+=1
for i in y:
    if i not in x:
        c+=1
print(c)