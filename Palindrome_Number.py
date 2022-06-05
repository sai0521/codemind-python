def palin(x):
    r=0
    n=x
    while x:
        y=x%10
        x=x//10
        r=r*10+y
    if r==n:
        return 1
    else:
        return 0

n=int(input())
for i in range(1,n+1):
    m=int(input())
    if palin(m):
        print('True')
    else:
        print('False')