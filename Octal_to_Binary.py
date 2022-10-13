for i in range(int(input())):
    m=int(input())
    ans=""
    while m:
        if m//10==0:
            st=""
            while m:
                y=m%2
                m=m//2
                st+=str(y)
            ans=st[::-1]+ans                
        else:
            n=m%10
            m=m//10
            t=3
            st=""
            while t:
                x=n%2
                n=n//2
                st+=str(x)
                t-=1
            ans=st[::-1]+ans
    print(ans)
        
