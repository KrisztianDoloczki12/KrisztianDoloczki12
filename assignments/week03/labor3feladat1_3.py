helyespin=input("Helyes pin:")
egyenleg=int(input("Egyenleg:"))
print("Kerem helyezze be a kartyat!")
pin=input("Kerem adja meg a pin kodot:")
for i in range(0,2):
    if pin==helyespin:
        felvett=int(input("Kerem adja meg a felvenni kivant osszeget:"))
        if felvett>egyenleg:
            print("A felvenni kivant osszeg tul magas!")
        else:
            egyenleg-=felvett
            print("Uj egyenleg:",egyenleg)
        break
    else:
        print("Helytelen pin, kerem probalkozzon ujra!")
        pin=input("Kerem adja meg a pin kodot:")
    if i == 1:
        print("Tul sok probalkozas!")