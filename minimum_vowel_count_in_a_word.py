n=input().split()
c=0
m=[]
for i in n:
    c=0
    for j in i:
        if j in "aeiou":
            c+=1
    m.append(c)
print(min(m))