for i in range(int(input())):
    n,m=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l3=[]
    l3.extend(l1)
    l3.extend(l2)
    l3.sort()
    print(*l3)