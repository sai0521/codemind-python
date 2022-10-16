n=input()
n=n.lower()
s=[]
for i in n:
    if i!=" " and n.count(i)==1:
        s.append(i)
s.sort()
for i in s:
    print(i,end="")