egyenleg=int(input("Kezdeti egyneleg:"))
print("0=kilepes")
while True:
    tranzakcio=int(input("Felvenni/levonni kivant osszeg(pozitiv/negativ):"))
    egyenleg+=tranzakcio
    if tranzakcio==0:
        print("A felhasznalo kilepett!")
        break
    print("Uj egyenleg:",egyenleg)
    if egyenleg<0:
        print("Helytelen muvelet!")
        break