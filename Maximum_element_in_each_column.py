n,m=map(int,input().split())
l=[]
for i in range(n):
    l1=list(map(int,input().split()))
    l.append(l1)
t=0
while m:
    a=[]
    for i in range(n):
        a.append(l[i][t])
    t+=1
    print(max(a))
    
        