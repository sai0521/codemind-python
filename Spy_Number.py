n=int(input())
s=0
p=1
while n>0:
    m=n%10
    n=n//10
    s=s+m
    p=p*m
if p==s:
    print("Spy Number")
else:
    print("Not Spy Number")