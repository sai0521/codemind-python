def reverse(x):
    r=0
    while x:
        y=x%10
        x//=10
        r=r*10+y
    return r

n=int(input())
m=n**2
a=reverse(n)
b=a**2
c=reverse(b)
if m==c:
    print("True")
else:
    print("False")
