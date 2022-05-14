n=int(input())
import math
l=int(math.log10(n))+1;
s=n*n
r=0
rev=0
while l!=0:
    m=s%10
    s=s//10
    r=r*10+m
    l-=1
while n>0:
    a=n%10
    n=n//10
    rev=rev*10+a
if r==rev:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")