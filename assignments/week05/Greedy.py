D=100
cel=400
megallok=[]
poz=0
i=0
kutak=[50,80,130,170,220,290,340,390]
aktualis_kut=0

while poz<cel:
    while i<len(kutak) and kutak[i]<=poz+100:
        aktualis_kut = i
        # print(aktualis_kut)
        # print(kutak[i])
        i=i+1
    megallok.append(kutak[aktualis_kut])
    # print(aktualis_kut)
    poz=kutak[aktualis_kut]
    print(poz)

print(megallok)