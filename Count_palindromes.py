def palin(x):
    r=0
    y=x
    while y:
        z=y%10
        y=y//10
        r=r*10+z
    if r==x:
        return 1
    else:
        return 0
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if palin(i):
        c+=1
print(c)