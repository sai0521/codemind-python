n=int(input())
l=list(map(int,input().split()))
c=len(l)
m=0
for i in l:
    m+=(i*pow(2,c-1))
    c-=1
print(m)