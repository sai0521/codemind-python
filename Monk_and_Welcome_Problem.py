n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
m=[]
for i in range(0,n):
    m.append(l1[i]+l2[i])
print(*m)