n=input()
for i in range(len(n)):
    if ord(n[i])>=48 and ord(n[i])<=57:
        if ord(n[i])%2!=0:
            print(int(n[i])**2,end='')