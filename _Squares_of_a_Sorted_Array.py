n=int(input())
arr=list(map(int,input().split()))
for i in range(0,n):
    arr[i]=arr[i]**2
for i in range(0,n-1):
    s=0
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
            s=1
    if s==0:
        break
for i in range(0,n):
    print(arr[i],end=' ')

           
