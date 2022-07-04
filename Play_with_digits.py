n=int(input())
l=list(map(int,input().split()))
m=[]
for i in l:
    j=i
    s=0
    while j:
        k=j%10
        j=j//10
        s=s+k
    m.append(s)
print(sum(m))