n=int(input())
l=list(map(int,input().split()))
m=int(input())
s=[]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
for i in l1:
    if m==l.count(i):
        s.append(i)
if s==[]:
    print(-1)
else:
    print(*s)