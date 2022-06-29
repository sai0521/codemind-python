a=int(input())
n=a
import math
l=int(math.log10(n))+1
s=0
while n:
    m=n%10
    n=n//10
    s+=pow(m,l)
    l-=1
if s==a:
    print("True")
else:
    print("False")