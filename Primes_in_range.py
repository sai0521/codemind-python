def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
m=int(input())
c=0
if n<2:
    n=2
for i in range(n,m+1):
    if prime(i)==1:
        c+=1
print(c)