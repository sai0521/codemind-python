def self_div(n):
    import math
    if n==0:
        return 0
    else:
        l=int(math.log10(n))+1
        c=0
        a=n
        while a:
           b=a%10
           a=a//10
           if b!=0 and n%b==0:
               c+=1
        if c==l:
            return 1
        else:
            return 0

n=int(input())
m=int(input())
for i in range(n,m+1):
        if self_div(i):
            print(i,end=' ')