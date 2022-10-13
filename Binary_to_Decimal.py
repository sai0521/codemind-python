for i in range(int(input())):
    m=input()
    m=m[::-1]
    ans=0
    t=0
    for i in m:
        if i=="1":
            ans+=pow(2,t)
        t+=1
    print(ans)