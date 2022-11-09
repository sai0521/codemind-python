for i in range(int(input())):
    n=int(input())
    if n==1:
        print(0)
    else:
        x=n
        c=0
        while x!=0:
            c=x
            x=x&(x-1)
        print(c-1)