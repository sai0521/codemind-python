n=int(input())
l=list(map(int,input().split()))
for i in range(0,n):
    if l[i]%2!=0:
        m=i
print(m)