N=int(input("Adja meg, hogy hany szamot szeretne beolvasni:"))
pozitiv=[]
paros=[]
paratlan=[]
for i in range(1,N+1):
    szam=int(input("szam:"))
    if szam>=0:
        pozitiv.append(szam)
        if szam%2==0:
            paros.append(szam)
        else:
             paratlan.append(szam)
print("paros:",paros)
print("pozitiv:",pozitiv)
print("paratlan:",paratlan)