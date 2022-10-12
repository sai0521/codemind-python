n=int(input())
l=list(map(int,input().split()))
m=int(input())
x=max(l)
s=[]
for i in l:
    if i+m>=x:
        s.append("True")
    else:
        s.append("False")
print(*s)