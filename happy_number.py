def happy(n):
    import math
    s=0
    while n:
        m=n%10
        n=n//10
        s=s+m**2
    l=int(math.log10(s))+1
    if l==1 and s!=1:
        return 0
    elif l==1 and s==1:
        return 1
    else:
        return happy(s)
        

n=int(input())
m=happy(n)
if m==1:
    print('True')
else:
    print('False')