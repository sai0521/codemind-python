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
c=0
for i in range(1,n+1):
    c=0
    if n%i==0:
        m=prime(i)
        if m==2 or m==3 or m==4 or m==0:
            c+=1
if c==1:
    print('Ugly Number')
else:
    print('Not Ugly Number')
        