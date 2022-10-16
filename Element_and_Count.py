n=int(input())
x=list(map(int,input().split()))
m=[]
l=[]
for i in x:
    if i not in l:
        l.append(i)
for i in l:
    m.append(i)
    m.append(x.count(i))
print(*m)