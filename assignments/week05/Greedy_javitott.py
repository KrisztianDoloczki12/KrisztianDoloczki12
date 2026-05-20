D=100
cel=400
megallok=[]
poz=0
i=0
kutak=[50,80,130,170,220,290,340,390]


while poz+D<cel:
    utolso = -1
    while i<len(kutak) and kutak[i]<=poz+D:
        utolso=i
        i+=1

    if utolso==-1:
        print("A cel nem erheto el!")
        break

    poz=kutak[utolso]
    megallok.append(poz)
else:
    print("Megallok:",megallok)