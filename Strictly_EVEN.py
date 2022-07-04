n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,n):
    if l[i]%2==0 and i%2==0:
        c+=1
    elif l[i]%2==0 and i%2!=0:
        c=0
        break
if c==0:
    print("False")
else:
    print("True")