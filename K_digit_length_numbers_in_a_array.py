
n,m=map(int,input().split())
l=list(map(int,input().split()))
#print(l)
c=0
for i in l:
    if i<0:
        i=-(i)
    if len(str(i)) == m:
        c+=1
print(c)