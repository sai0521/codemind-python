def prime(x):
    c=0
    for i in range(1,x+1):
        if x%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0

n=int(input())
r=0
if prime(n):
    while n:
        m=n%10
        n=n//10
        r=r*10+m
    if prime(r):
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')
 