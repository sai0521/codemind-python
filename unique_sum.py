n=int(input())
l=list(map(int,input().split()))
#print(l)
s=[]
for i in l:
    if i not in s:
        s.append(i)
print(sum(s))
    