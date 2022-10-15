l=input()
c=0
j=len(l)-1
for i in range(0,len(l)//2):
    if l[i] in "aeiouAEIOU" and l[j] not in "aeiouAEIOU" and l[i] not in " " and l[j] not in " ":
        c+=1
        #print(l[i],l[j])
    elif l[i] not in "aeiouAEIOU" and l[j] in "aeiouAEIOU" and l[i] not in " " and l[j] not in " ":
        c+=1
        #print(l[i],l[j])
    j-=1
print(c)