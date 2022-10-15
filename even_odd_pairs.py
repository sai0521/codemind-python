n=int(input())
l=list(map(int,input().split()))
#print(l)
a=[]
b=[]
for i in l:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
k=1
i=0
while len(a)!=n:
    a.insert(k,b[i])
    k+=2
    i+=1
if len(a)%2!=0:
    a.append(0)
print(*a)