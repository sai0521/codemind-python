n=int(input())
st=""
while n:
    x=n%2
    n=n//2
    if x==1:
        st+="0"
    else:
        st+="1"
t=0
ans=0
for i in st:
    if i=="1":
        ans+=pow(2,t)
    t+=1
print(ans)   