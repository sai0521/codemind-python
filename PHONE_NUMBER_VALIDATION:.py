n=int(input())
c=0
while n>0:
    m=n%10
    n=n//10
    c+=1
if c==10:
    print('Valid')
else:
    print("Invalid")