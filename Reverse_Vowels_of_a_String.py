n=input()
m=[]
for i in range(len(n)):
    if n[i] in "aeiouAEIOU":
        m.append(n[i])
s=m.copy()
s.reverse()
n=list(n)
j=0
for i in range(len(n)):
    if n[i] in m:
        print(s[j],end='')
        j+=1
    else:
        print(n[i],end='')