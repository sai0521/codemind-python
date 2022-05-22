n=int(input())
import math
c=0
arr=list(map(int,input().split()))
for i in range(0,n):
    len=int(math.log10(arr[i]))+1
    if len%2==0:
        c+=1
print(c)  
                