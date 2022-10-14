l=input()
m=[]
for i in l:
    if i!=",":
        m.append(int(i))
a=[]
for i in m:
    s=0
    for j in range(1,int(i+1)):
        if i%j==0:
            s+=j
    if s in m:
        a.append(i)
a.sort()
if a==[]:
    print(-1)
else:
    print(*a)