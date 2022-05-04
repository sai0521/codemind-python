n=int(input())
b=n
a=n*n
s=0
while a>0:
    m=a%10
    a=a//10
    s=s+m
if s==b:
    print("Neon Number")
else:
    print("Not Neon Number")