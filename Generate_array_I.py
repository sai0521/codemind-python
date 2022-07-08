n=int(input())
l=list(map(int,input().split()))
m=[]
for i in range(0,n,2):
    for j in range(i+1,n):
        x=l[j]
        while x:
            m.append(l[i])
            x-=1
        break
print(*m)