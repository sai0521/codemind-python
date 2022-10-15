n=input()
n=n.split(" ")
for i in n:
    x=ord(min(i))
    y=ord(max(i))
    print(abs(x-y),end=" ")