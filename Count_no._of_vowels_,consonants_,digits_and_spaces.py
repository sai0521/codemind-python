n=input()
vc=0
cc=0
sc=0
dc=0
for i in range(len(n)):
    if n[i] in "aeiouAEIOU":
        vc+=1
    elif n[i] in " ":
        sc+=1
    elif n[i] in "1234567890":
        dc+=1
    else:
        cc+=1
print("Vowels:",vc)
print("Consonants:",cc)
print("Digits:",dc)
print("White spaces:",sc)
        