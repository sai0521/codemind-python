n=int(input())
l=list(map(int,input().split()))
#print(l)
s=[]
for i in l:
    if i not in s:
        if i%2!=0:
            s.append(i)
print(len(s))
    