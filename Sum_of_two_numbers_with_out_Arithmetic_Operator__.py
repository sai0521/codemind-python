a,b=map(int,input().split())
while(b):
    c=a&b
    b=c<<1
    a=a^b
print(a)