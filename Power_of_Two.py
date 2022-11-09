n=int(input())
i=0
while 1:
    k=2**i
    if n==k:
        print(True)
        break
    if k>n:
        print(False)
        break
    i+=1