def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
n=int(input())
m=int(input())
i=1
while 1:
    s=n+m+i
    if prime(s):
        print(i)
        break
    i+=1