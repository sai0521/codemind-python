n=input()
c=0
m=[]
s=[]
for i in n:
    if i in "aeiou":
        m.append(i)
for j in "aeiou":
    if j not in m:
        c+=1
        s.append(j)
if c==0:
    print(0)
else:
    print(*s)