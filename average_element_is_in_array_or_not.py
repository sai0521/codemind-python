n=int(input())
l=list(map(int,input().split()))
m=sum(l)//n
if m in l:
    print("True")
else:
    print("False")