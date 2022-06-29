n=input()
n=n.split(" ")
m=[]
for i in n:
    c=0
    for j in i:
        if j in "aeiouAEIOU":
            c+=1
    m.append(c)
print(*m)
            