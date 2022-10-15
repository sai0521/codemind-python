n=input()
n=n.lower()
#print(n)
m=input()
m=m.lower()
s=[]
for i in n:
    if i!=" " and i in m and i not in s:
        s.append(i)
s.sort()
for i in s:
    print(i,end="")
if s==[]:
    print(-1)