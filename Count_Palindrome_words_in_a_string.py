n=input()
m=n.lower()
m=m.split()
c=0
for i in m:
    j=i[::-1]
    if i==j:
        c+=1
print(c)