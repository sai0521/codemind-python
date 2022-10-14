import math
n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    x=math.sqrt(i)
    if x==int(x):
        s+=int(i)

print(s)