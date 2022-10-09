n=int(input())
s=0
for i in range(n):
    m=input()
    if '+' in m:
        s+=1
    elif '-' in m:
        s-=1
print(s)