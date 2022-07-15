n=input()
n=n.lower()
c=0
for i in n:
    if i not in "abcdefghijklmnopqrstuvwxyz1234567890 ":
        c+=1
print(c)