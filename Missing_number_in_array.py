for i in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
   
    for i in range(1,n+1):
        if i not in l1:
            print(i)
