n=int(input())
m=int(input())
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
r=0
for i in range(1,m):
    if m%i==0:
        r+=i
if r==n and s==m:
    print("Amicable")
else:
    print("Not Amicable")
    