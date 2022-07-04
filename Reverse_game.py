n=int(input())
l=list(map(int,input().split()))
for i in l:
    r=0
    j=i
    while j:
        k=j%10
        j=j//10
        r=r*10+k
    print(r,end=" ")