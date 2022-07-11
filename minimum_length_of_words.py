n=input()
n=n.split(" ")
m=[]
for i in n:
    m.append(len(i))
print(min(m))