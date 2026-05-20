import math

szam=int(input("Szam:"))

prim=True

if szam<=1:
    print("Helytelen ertek!")

for i in range(2,int(math.sqrt(szam))+1):
    if szam%i==0:
       prim=False
       break

if prim:
    print(szam, "primszam")
else:
    print(szam, "nem primszam")