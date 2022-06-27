n=input()
n=n.split(" ")
m=[]
for i in range(len(n)):
        m.append(n[i][::-1])
print(*m[::-1])