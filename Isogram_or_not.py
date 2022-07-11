n=input()
m=""
for i in n:
    if i not in m:
        m+=i
if n==m:
    print("True")
else:
    print("False")