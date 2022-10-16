n=input()
m=input()
n=n.lower()
m=m.lower()
n=n.split(" ")
m=m.split(" ")
#print(n,m)
c=0
for i in n:
    if i in m:
        c+=1
print(c)