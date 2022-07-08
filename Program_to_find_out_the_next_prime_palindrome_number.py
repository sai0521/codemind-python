def prime(x):
    if x==1:
        return 0
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return 0
    return 1

def palin(a):
    r=0
    b=a
    while b:
        c=b%10
        b//=10
        r=r*10+c
    if r==a:
        return 1
    else:
        return 0



n=int(input())
m=n+1
while 1:
    if prime(m):
        if palin(m):
            print(m)
            break
    m+=1
        