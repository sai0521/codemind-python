n=input()
m=""
for i in n:
    if i in 'aeiou':
        m+=i
        c=0
for i in 'aeiou':
    if i not in m:
        print(i,end=" ")
        c=1
if c==0:
    print(0)