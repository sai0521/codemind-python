import math
for i in range(int(input())):
    n=int(input())
    #print(n,end=" ")
    if n%2==0:
        if (n/2)%2!=0:
            print(3)
        else:
            print(n+3)
    else:
        if (math.ceil(n/2))%2==0:
            print(3)
        else:
            print(n)
        