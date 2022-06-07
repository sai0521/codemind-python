n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    for j in range(0,n):
        if i!=j and a[i]==a[j]:
            print(a[i])
            c+=1
            break
    if c==1:
        break
            