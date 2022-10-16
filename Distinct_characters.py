n=input()
n=n.lower()
s=[]
for i in n:
    if i not in s and i!=" ":
        s.append(i)
s.sort()
for i in s:
    print(i,end="")