def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 1
    else :
        return 0
n=int(input())
c=0

for i in range(1,n):
    if prime(i):
        for j in range(i+1,n+1):
            if prime(j):
                if i*j==n:
                    c+=1
                    a=i
                    b=j
                    break
if c==1:
    print(a,b,end=' ')
else:
    print('-1')