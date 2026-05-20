szo=input("Adj meg egy szot:")
maganhangzok=0
maganhangzo_lista="aeiou"
for betu in szo.lower():
    if betu in maganhangzo_lista:
        maganhangzok+=1
print("A szövegben", maganhangzok, "magánhangzó található.")