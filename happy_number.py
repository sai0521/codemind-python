def happy(x):
    s=0
    while x:
        y=x%10
        x//=10
        s+=pow(y,2)
    if s<=9:
        return s
    else:
        return happy(s)

n=int(input())
m=happy(n)
if m==1 or m==7:
    print("True")
else:
    print("False")
