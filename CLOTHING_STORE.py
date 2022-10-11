n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    if i not in s:
        s.append(i)
x=0
for i in s:
    x+=l.count(i)//2
print(x)