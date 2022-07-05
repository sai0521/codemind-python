n=int(input())
l=list(map(int,input().split()))
m=[]
for i in l:
    if l.count(i)==i and i not in m:
        m.append(i)
if m==[]:
    print(-1)
else:
    print(*m)