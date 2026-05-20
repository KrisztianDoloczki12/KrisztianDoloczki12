import random

lista=[random.randint(0,100) for i in range(1,11)]
print("A lista:",lista)

forditott_lista=[]

for i in range(len(lista)-1,-1,-1):
    forditott_lista.append(lista[i])

print("Forditott lista:",forditott_lista)