n=int(input())
m=n
import math
c=int(math.log10(n))+1
s=0
while m:
    r=m%10
    m=m//10
    s+=pow(r,c)
    c-=1
if s==n:
    print("True")
else:
    print("False")