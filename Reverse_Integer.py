n=int(input())
r=0
if n>0:
    while n!=0:
        m=n%10
        n=n//10
        r=r*10+m
    print(r)    
else:
    n=-(n)
    while n!=0:
        m=n%10
        n=n//10
        r=r*10-m
    print(r)