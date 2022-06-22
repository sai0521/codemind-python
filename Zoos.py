n=input()
c=0
d=0
for i in range(len(n)):
    if n[i]=='z':
        c+=2
    elif n[i]=='o':
        d+=1
if c==d:
    print("Yes")
else:
    print("No")
        