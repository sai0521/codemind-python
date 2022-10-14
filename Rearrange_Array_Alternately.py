for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=[]
    if n%2==0:
        while len(l):
            x=max(l)
            y=min(l)
            m.append(x)
            m.append(y)
            l.pop(l.index(x))
            l.pop(l.index(y))
    else:
        while len(l)!=1:
            x=max(l)
            y=min(l)
            m.append(x)
            m.append(y)
            l.pop(l.index(x))
            l.pop(l.index(y))
        m.append(l[0])
    print(*m)