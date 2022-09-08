n=input()
n=n.split(":")
a=int(n[0])
b=int(n[1])
if(a==12):
    a=0
if(b==60):
    b=0
    a+=1
    if(a>12):
        h=h-12
ha = 0.5*(a*60+b)
ma = 6*b
ans=abs(ha-ma)
if(ans>180):
    ans=360-ans
print(ans)