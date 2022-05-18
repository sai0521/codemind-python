n=int(input())
arr=list(map(int,input().split()))
se=0
so=0
for i in range(0,n):
    if i%2==0:
        se=se+arr[i]
    else:
        so=so+arr[i]
if so-se==0:
    print("YES")
else:
    print("NO")