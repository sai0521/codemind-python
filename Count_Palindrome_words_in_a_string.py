def palin(x):
    y=x
    z=x[::-1]
    if y==z:
        return 1
    else:
        return 0

n=input()
n=n.lower()
n=n.split(" ")
c=0
for i in n:
    if palin(i):
        c+=1
print(c)