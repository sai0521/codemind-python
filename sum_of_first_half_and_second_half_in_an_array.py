n=int(input())
l=list(map(int,input().split()))
m=(len(l)//2)
s=0
s1=0
for i in range(0,m):
    s+=l[i]
for i in range(m,n):
    s1+=l[i]
print(s)
print(s1)