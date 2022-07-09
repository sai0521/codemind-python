def prime(x):
    if x==1:
        return 0
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return 0
    return 1


n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        if prime(i):
            if i==2 or i==3 or i==5:
                c=1
            else:
                c=0
                break
if n==1 :
    print("Ugly Number")
elif c==0:
    print("Not Ugly Number")
else:
    print("Ugly Number")