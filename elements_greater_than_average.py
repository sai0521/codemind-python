n=int(input())
l=list(map(int,input().split()))
m=sum(l)//n
c=0
for i in l:
    if i>=m:
        c+=1
print(c)