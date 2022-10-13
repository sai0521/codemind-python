for i in range(int(input())):
    m=int(input())
    st=""
    while m:
        x=m%2
        m=m//2
        st+=str(x)
    print(st[::-1])