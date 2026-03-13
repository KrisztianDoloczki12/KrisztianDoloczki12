N=int(input("Adja meg, hogy hany szamot szeretne beolvasni:"))
sum=0
for i in range(1,N+1):
    szam=int(input("szam:"))
    if szam>=0:
        sum+=szam
print("A pozitiv szamok osszege:",sum)