n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    c=0
    c1=0
    for j in range(a,b+1):
        c=0
        m=j%10
        if m==2 or m==3 or m==9 :
            c+=1
        if c==1:
            c1+=1
    print(c1)
