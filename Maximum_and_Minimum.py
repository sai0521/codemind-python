n=int(input())
l=list(map(int,input().split()))
m=[]
x=[]
for i in l:
    if i not in m:
        m.append(i)
for i in m:
    if i==l.count(i):
        x.append(i)
if x==[]:
    print(-1)
else:
    print(min(x),max(x))