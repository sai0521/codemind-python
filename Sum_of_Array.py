n=int(input())
l=list(map(int,input().split()))
es=0
os=0
for i in range(0,n):
    
    es+=l[i]
print(abs(es))