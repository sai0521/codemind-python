n,m=map(int,input().split())
if n-1==m or n+1==m or n==1 and m==10 or m==1 and n==10:
    print("Yes")
else:
    print("No")