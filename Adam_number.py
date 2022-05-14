n=int(input())
rev=0
r=0
temp=n
sq1=n*n
while n:
    m=n%10
    n=n//10
    rev=rev*10+m
sq2=rev*rev
while sq2:
    p=sq2%10
    sq2=sq2//10
    r=r*10+p
if r==sq1:
    print('True')
else:
    print('False')