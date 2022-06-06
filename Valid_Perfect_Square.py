n=int(input())
for i in range(1,n+1):
    m=int(input())
    c=0
    for j in range(1,m):
        if j*j==m:
            c+=1
            break
    if c==1:
        print('True')
    else:
        print('False')