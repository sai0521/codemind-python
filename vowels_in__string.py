n=input()
c=0
m=[]
for i in n:
    if i in "aeiouAEIOU" and i not in m:
        c+=1
        m.append(i)

if c==0:
    print(-1)
else:
    print(*m)