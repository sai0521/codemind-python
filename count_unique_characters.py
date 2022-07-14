n=input()
m=n.lower()
m=m.split(" ")
x=""
for i in m:
    x+=i
s=""
for i in x:
    if x.count(i)==1:
        s+=i
print(len(s))
