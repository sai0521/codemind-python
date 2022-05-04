n=int(input())
r=0
while n>0:
    m=n%10
    n=n//10
    if r<m:
        r=m
print(r)