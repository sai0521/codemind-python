n=int(input())
a=list(map(int,input().split()))
m=max(a)
import math
l=int(math.log10(m))+1
c=0
for i in a:
    len=int(math.log10(i))+1
    if len==l:
        c+=1
print(c)