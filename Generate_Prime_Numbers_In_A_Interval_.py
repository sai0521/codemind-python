def prime(n):
    c=0
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1

n=int(input())
m=int(input())
for i in range(n,m+1):
    if prime(i):
        print(i)