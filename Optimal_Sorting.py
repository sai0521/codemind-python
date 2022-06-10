a=int(input())
for i in range(0,a):
    n=int(input())
    a=list(map(int,input().split()))
    m=sorted(a)
    if m==a:
        print('0')
    else:
        print(max(m)-min(m))