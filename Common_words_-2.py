n=input()
n=n.split(" ")
m=input()
m=m.split(" ")
c=0
for i in n:
    if i in m and m.count(i)==1 and n.count(i)==1:
        c+=1
        #print(i)
print(c)