n=input()
n=n.split(" ")
m=[]
for i in n:
    print(abs(ord(min(i))-ord(max(i))),end=" ")