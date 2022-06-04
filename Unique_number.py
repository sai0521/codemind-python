n=int(input())
s=[]
a=[]
k=c=0
while n:
    m=n%10
    n=n//10
    s.append(m)
    k+=1
for i in s:
    c=0
    for j in s:
        if i==j:
            c+=1
    if c==1:
        a.append(i)
if s==a:
    print('Unique Number')
else:
    print('Not Unique Number')