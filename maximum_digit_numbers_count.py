import math
n=int(input())
l=list(map(int,input().split()))
d=0
for i in l:
    c=len(str(i))
    if c>d:
        d=c
for i in l:
    if len(str(i)) == d:
        print(i,end=" ")