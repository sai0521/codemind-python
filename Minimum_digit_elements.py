n=int(input())
l=list(map(int,input().split()))
m=min(l)
import math
c=int(math.log10(m))+1
c1=0
for i in l:
    x=int(math.log10(i))+1
    if x==c:
        c1+=1
print(c1)