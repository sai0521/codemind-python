def count(n):
    co=0
    if n==0:
        return 1
    if n<0:
        n=-(n)
    while n:
        n=n//10
        co+=1
        
    return co

n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    if i not in s:
        s.append(count(i))
print(*s)