n=int(input())
l=list(map(int,input().split()))
m=[]
for i in l:
    if i!=0:
        m.append(i)
while len(m)!=n:
    m.append(0)
print(*m)
        

        