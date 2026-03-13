szamlalo=1
while(True):
    szam = float(input("Szam:"))
    if szamlalo==1:
        min=szam
        max=szam
    if szam>max:
        max=szam
    if szam<min:
        min=szam
    szamlalo=szamlalo+1
    if szam==0:
        print("Max:",max,"Min:",min)
        break