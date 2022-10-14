a,b,c=map(int,input().split())
l=list(map(int,input().split()))
while b:
    x=l[-1]
    l.pop(l.index(x))
    l.insert(0,x)
    b-=1
for i in range(c):
    n=int(input())
    print(l[n])