n=input()
n=n.lower()
s=[]
for i in n:
    if i!=" " and n.count(i)==1:
        s.append(i)
if s==[]:
    print(-1)
else:
    print(s[0])