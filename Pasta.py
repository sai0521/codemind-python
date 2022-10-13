n,m=map(int,input().split())
l=list(map(int,input().split()))
s=list(map(int,input().split()))
c=0
for i in range(m):
    if s[i] in l:
        l.pop(l.index(s[i]))
        c+=1
if c==m:
    print("Yes")
else:
    print("No")