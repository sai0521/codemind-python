n=int(input())
l=list(map(int,input().split()))
z=[]
for i in l:
    if i not in z:
        z.append(i)
print(*z)