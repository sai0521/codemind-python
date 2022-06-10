def reverse(n):
    r=0
    while n:
        m=n%10
        n=n//10
        r=r*10+m
    return r
n=int(input())
while 1:
    n=n+reverse(n)
    if n==reverse(n):
        print(n)
        break