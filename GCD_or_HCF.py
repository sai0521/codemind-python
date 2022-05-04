n,m=map(int,input().split())
max=0
for i in range(1,n*m):
    if n%i==0 and m%i==0:
        if max<i:
            max=i
print(max)