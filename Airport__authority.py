n=int(input())
b=[]
c=0
for i in range(0,n):
    m=int(input())
    b.append(m)
p=int(input())
for i in b:
    if i>p:
        c+=2
    else:
        c+=1
print(c)