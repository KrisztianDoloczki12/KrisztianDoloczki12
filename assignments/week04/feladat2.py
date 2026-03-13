paros=0
negativ=0

while(True):
    szam=int(input("szam:"))
    if szam==0:
        break
    if szam%2==0:
        paros+=1
    if szam<0:
        negativ+=1
print("paros:",paros)
print("negativ:",negativ)