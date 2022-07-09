def prime(x):
    if x==1:
        return 0
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return 0
    return 1
    
def rev(a):
    r=0
    while a:
        b=a%10
        a//=10
        r=r*10+b
    return r

n=int(input())
if prime(n):
    m=rev(n)
    if prime(m):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")