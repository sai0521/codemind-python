n=int(input())
for i in range(1,n+1):
    m=input()
    c=0
    for j in range(len(m)):
        if m[j] in "1234567890":
            c+=1
    if len(m)==c:
        print("True")
    else:
        print("False")