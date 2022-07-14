n=input()
n=n.lower()
m=""
for i in n:
    if i  not in m and i!=" ":
        m+=i

print(len(m))