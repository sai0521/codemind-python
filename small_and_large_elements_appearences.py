m=input()
n=""
for i in m:
    if i!=" ":
        n+=i
x=max(n)
y=min(n)
a=n.count(x)
b=n.count(y)
print(y,b,x,a)