n=int(input())
l=list(map(int,input().split()))
m=[]
for i in l:
    if i%2==0:
        m.append(i)
for i in l:
    if i%2!=0:
        m.append(i)
print(*m)