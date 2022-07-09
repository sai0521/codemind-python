n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
s=[]
for i in l1:
    if i in l2 and i not in s:
        s.append(i)
for i in l2:
    if i in l1 and i not in s:
        s.append(i)
print(*s)