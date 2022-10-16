n=input()
c=0
#print(n)
for i in n:
    if i not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ":
        c+=1
        #print(i)
print(c)