for i in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    c=0
    for i in range(0,n):
        for j in range(i+1,n):
            x=l1[i]+l1[j]
            if x in l1:
                c+=1
    if c==0:
        print(-1)
    else:
        print(c)