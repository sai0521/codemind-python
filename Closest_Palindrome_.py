def palin(p):
    q=p
    rev=0
    while q:
        w=q%10
        q=q//10
        rev=rev*10+w
        
    if rev==p:
        return 1
    else:
        return 0



n=int(input())
t1=n-1
t2=n+1

s=[]

while 1:
    if palin(t1):
        s.append(t1)
        break
    t1-=1

while 1:
    if palin(t2):
        s.append(t2)
        break
    t2+=1
    
a=abs(n-s[-1])
b=abs(n-s[-2])
c=min(a,b)
if b==a:
    print(s[-2],s[-1])
elif c==a:
    print(s[-1])
else:
    print(s[-2])