n=int(input())
arr=list(map(int,input().split()))
for i in range(0,n):
    c=0
    for j in range(0,n):
        if i!=j:
            if arr[i]>arr[j]:
                c+=1
    print(c,end=' ')
                