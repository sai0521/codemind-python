def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

n,m=map(int,input().split())
print(gcd(n,m))