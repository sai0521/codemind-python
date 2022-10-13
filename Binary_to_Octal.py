def con_bin(a):
    b=0
    t=0
    a=a[::-1]
    for i in a:
        if i=="1":
            b+=pow(2,t)
        t+=1
    return str(b)
    
def bin_to_oct(x):
    ans=""
    for i in range(0,len(x)-2,3):
        s=[]
        s.append(x[i])
        s.append(x[i+1])
        s.append(x[i+2])
        ans+=con_bin(s)
    return ans

for i in range(int(input())):
    m=input()
    m=list(m)
    if len(m)%3==0:
        n=bin_to_oct(m)
    else:
        while(len(m)%3):
            m.insert(0,0)
        n=bin_to_oct(m)
            
    print(n)
