n=input()
n=n.split(" ")
m=[]
for i in range(len(n)):
        m.append(n[i])
print(*m[::-1])