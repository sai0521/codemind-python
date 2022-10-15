n=int(input())
l1=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
x=[]
for i in range(0,n):
    x.insert(l2[i],l1[i])
print(*x)