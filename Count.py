n=int(input())
a=list(map(int,input().split()))
oc=0
ec=0
for i in a:
    if i%2==0:
        oc+=1
    else:
        ec+=1
print(oc,ec)