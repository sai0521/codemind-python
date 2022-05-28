p,r,t=map(int,input().split())
a=1+(r/100)
b=a**t
c=p*b
print("{:.2f}".format(c))