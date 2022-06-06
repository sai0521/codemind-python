def digits(x):
    s=0
    if x<=9:
        return x
    else:
        a=x
        while a:
            b=a%10
            a=a//10
            s=s+b
        return digits(s)


n=int(input())
m=digits(n)
print(m)