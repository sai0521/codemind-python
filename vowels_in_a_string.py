n=input()
m=input()
a=0
flg=0
for i in n:
    if m==i:
        a=n.index(i)
        flg=1
        break
if flg==0:
    print("False")
else:
    print("True")
    print(a)
    