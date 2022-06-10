n=int(input())
a=0
b=1
c=a+b
flag=0
if n==a or n==b :
    print('True')
else:
    while c<=n:
        if c==n:
            flag=1
            break
        a=b
        b=c
        c=a+b
    if flag==1:
        print('True')
    else:
        print('False')