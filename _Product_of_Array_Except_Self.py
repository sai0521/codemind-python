n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    s=1
    for j in range(0,n):
        if i!=j:
            s=s*a[j]
    print(s,end=' ')
            