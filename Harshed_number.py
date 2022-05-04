n=int(input())
b=n
r=0
while n>0:
    m=n%10
    n=n//10
    r=r+m
if b%r==0:
    print("True")
else:
    print("False")