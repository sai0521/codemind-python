def prime(x):
    if x==1 or x==0:
        return 0
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return 0
    return 1

n=int(input())
l=list(map(int,input().split()))
m=int(input())
c=0
for i in l:
    if i<=m and prime(i):
        c+=1
print(c)