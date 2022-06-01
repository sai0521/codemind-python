n=int(input())
m=int(input())
for i in range(1,m+1):
    x,y=map(int,input().split())
    if x<n or y<n:
        print('UPLOAD ANOTHER')
    else:
        if x==y:
            print('ACCEPTED')
        else:
            print('CROP IT')