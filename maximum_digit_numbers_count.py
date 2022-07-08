def count(x):
    c=0
    if x<0:
        x=-(x)
    while x:
        x=x//10
        c+=1
    return c

n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    a.append(count(i))
c=max(a)
s=[]
for i in l:
    if c==count(i) and i not in s:
        s.append(i)
print(*s)