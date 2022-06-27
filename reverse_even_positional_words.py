n=input()
n=n.split(" ")
m=[]
for i in range(len(n)):
    if i%2==0:
        m.append(n[i][::-1])
    else:
        m.append(n[i])
print(*m)