def palin(p):
    q=p
    rev=0
    while q:
        w=q%10
        q=q//10
        rev=rev*10+w
        
    if rev==p:
        return 1
    else:
        return 0

def prime(x):
    if x==1 or x==0:
        return 0
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return 0
    return 1
    
n=int(input())
t2=n+1
s=[]
while 1:
    if palin(t2):
        if prime(t2):
            print(t2)
            break
    t2+=1

