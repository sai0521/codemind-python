n=input()
n=n.lower()
m=""
for i in n:
    if n.count(i)==1 and i!=" ":
        m+=i
m="".join(sorted(m))
print(m)