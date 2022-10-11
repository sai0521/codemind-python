n=int(input())
l=list(map(int,input().split()))
x=sum(l)//n
c=0
for i in l:
    if i<=x:
        c+=1
print(c)