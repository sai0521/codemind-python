n=input()
m=input()
n=n.lower()
m=m.lower()
n=n.split()
m=m.split()
c=0
for i in n:
    if i in m:
        c+=1
print(c)
