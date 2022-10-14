for i in range(int(input())):
    a,b=map(int,input().split())
    l1=list(map(int,input().split()))
    x=y=s=fl=0
    for i in range(0,a):
        s=0
        for j in range(i,a):
            s+=l1[j]
            if s==b:
                x=i+1
                y=j+1
                fl=1
                break
            if s>b:
                break
        if fl==1:
            break
    if x==0 and y==0:
        print(-1)
    else:
        print(x,y)