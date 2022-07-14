n=input()
n=n.split(" ")
m=[]
c=0
for i in n:
    c=0
    for j in i:
        if j in "aeiou":
            c+=1
    m.append(c)
print(max(m))