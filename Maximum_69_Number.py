n=int(input())
m=[]
c=[]
a=n
while a:
    b=a%10
    a=a//10
    c.append(b)
c=c[::-1]
for i in range(len(c)):
    if c[i]==6:
        c[i]=9
        break
for i in c:
    print(i,end="")
