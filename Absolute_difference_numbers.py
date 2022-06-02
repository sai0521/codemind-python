def reverse(x):
    r=0
    while x:
        y=x%10
        x=x//10
        r=r*10+y
    return r

def digits(a,c):
    rev=0
    while a:
        b=a%10
        a=a//10
        rev=rev*10+b
        c-=1
        if c==0:
            break
    return rev
    
    
n,c=map(int,input().split())

m=reverse(n)
h=digits(n,c)
first=digits(m,c)
last=reverse(h)
ans=first-last
if ans<0:
    ans=-(ans)
print(ans)