N=int(input("Adja meg, hogy hany szamot szeretne beolvasni:"))
negativ=False
nagyobb=False
for i in range(1,N+1):
    szam=int(input("szam:"))
    if szam>100:
        nagyobb=True
        print("Nagyobb ertek mint 100")
        break
    elif szam<0:
        negativ=True
        print("Negativ ertek")
        break
    if i==N:
        print("Nem volt negativ ertek vagy nagyobb ertek mint 100")
