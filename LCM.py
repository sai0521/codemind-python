n,m=map(int,input().split())
if n>m:
    x=n
else:
    x=m
while 1:
    if x%n==0 and x%m==0:
        print(x)
        break
    x+=1
    