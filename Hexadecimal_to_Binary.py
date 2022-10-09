for i in range(int(input())):
    a0="0000"
    a1="0001"
    a2="0010"
    a3="0011"
    a4="0100"
    a5="0101"
    a6="0110"
    a7="0111"
    a8="1000"
    a9="1001"
    aa="1010"
    ab="1011"
    ac="1100"
    ad="1101"
    ae="1110"
    af="1111"
    m=input()
    s=""
    for i in m:
        if i=="0":
            s+=a0
        elif i=="1":
            s+=a1
        elif i=="2":
            s+=a2
        elif i=="3":
            s+=a3
        elif i=="4":
            s+=a4
        elif i=="5":
            s+=a5
        elif i=="6":
            s+=a6
        elif i=="7":
            s+=a7
        elif i=="8":
            s+=a8
        elif i=="9":
            s+=a9
        elif i=="A":
            s+=aa
        elif i=="B":
            s+=ab
        elif i=="C":
            s+=ac
        elif i=="D":
            s+=ad
        elif i=="E":
            s+=ae
        elif i=="F":
            s+=af
    print(s)
            
    