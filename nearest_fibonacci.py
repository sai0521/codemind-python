n=int(input())
s=[1,1]
k=0
while 1:
    x=s[k]+s[k+1]
    s.append(x)
    if x>n:
        break
    k+=1
a=abs(n-s[-1])
b=abs(n-s[-2])
c=min(a,b)
if b==a:
    print(s[-2],s[-1])
elif c==a:
    print(s[-1])
else:
    print(s[-2])