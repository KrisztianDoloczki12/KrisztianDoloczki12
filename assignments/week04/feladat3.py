N=int(input("Adja meg, hogy hany szamot szeretne beolvasni:"))
for i in range(1,N+1):
    szam=int(input("szam:"))
    if i==1:
        max=szam
    if szam>max:
        max=szam
        pozicio=i
print("max:",max,"pozicioja:",pozicio)
