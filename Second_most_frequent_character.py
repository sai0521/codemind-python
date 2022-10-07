str=input()
arr=[0]*256
m=0
sm=0
i=0
for i in range(len(str)):
    if str[i]!=' ':
        num=ord(str[i])
        arr[num]+=1
for i in range(256):
    if arr[i] > arr[m]:
        sm=m
        m=i
    elif arr[i]>arr[sm] and arr[i]!=arr[m]:
        sm=i
x=sm
if x==0:
    print(-1)
else:
    print(chr(sm))