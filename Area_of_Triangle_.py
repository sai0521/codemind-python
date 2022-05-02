a,b,c=map(float,input().split())
import math
s=(a+b+c)/2
p=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("{:.2f}".format(p))