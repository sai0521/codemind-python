n=int(input())
arr=list(map(int,input().split()))
for i in range(n-1,int(n/2)-1,-1):
    print(arr[i],end=' ')
for i in range(0,int(n/2)):
    print(arr[i],end=' ')