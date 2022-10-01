n=int(input())
a=n
x=[]
while a:
    b=a%10
    a=a//10
    l=""
    temp=3
    while temp:
        c=b%2
        b=b//2
        l+=str(c)
        temp-=1
    x+=l
x=x[::-1]
str(x)
if x[0]=='0':
    x.pop(0)
if x[0]=='0':
    x.pop(0)
        
for i in x:
    print(i,end="")
