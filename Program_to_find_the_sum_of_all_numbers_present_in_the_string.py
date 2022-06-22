n=input()
s=0
for i in range(len(n)):
    if n[i] in "1234567890":
        s+=int(n[i])
print(s)