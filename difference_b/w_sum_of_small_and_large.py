n=input()
n=n.split(" ")
mi=[]
ma=[]
for i in n:
    mi.append(min(i))
    ma.append(max(i))
mis=0
mas=0
for i in mi:
    mis+=ord(i)
for i in ma:
    mas+=ord(i)
print(abs(mas-mis))
