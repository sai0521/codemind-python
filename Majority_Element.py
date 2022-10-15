n=int(input())
l=list(map(int,input().split()))
m=n//2
for i in l:
    if l.count(i)>m:
        print(i)
        break