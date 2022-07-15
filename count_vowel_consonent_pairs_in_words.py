n=input().split()
c=0
for i in n:
    a=0
    b=-1
    while 1:
        if i[a] in "aeiou" and i[b] not in "aeiou":
            c+=1
        elif i[a] not in "aeiou" and i[b] in "aeiou":
            c+=1
        if a==(len(i)//2)-1:
            break
        a+=1
        b-=1
print(c)