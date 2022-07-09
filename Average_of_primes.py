def prime(x):
    if x<=1:
        return 0
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return 0
    return 1

n=int(input())
l=list(map(int,input().split()))
s=c=0.0
for i in l:
    if prime(i):
        s+=i
        c+=1
if c==0:
    print(-1)
else:
    avg=s/c
    print("{:.2f}".format(avg))