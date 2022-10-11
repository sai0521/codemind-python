for i in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    while(b):
        x=l[-1]
        l.pop(a-1)
        l.insert(0,x)
        b-=1
    print(*l)