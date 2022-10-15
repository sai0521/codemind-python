n=input()
n=n.lower()
#print(n)
m=input()
m=m.lower()
s=[]
x=[]

for i in n:
    if i!=" " and i in m and i not in s:
        s.append(i)

for i in n:
    if i not in x and i not in s and i!=" ":
        x.append(i)
for i in m:
    if i not in x and i not in s and i!=" ":
        x.append(i)
        
#print(x)
#print(s)

if x==[]:
    print(-1)
else:
    print(len(x))