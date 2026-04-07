import random

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

def rekurziv_osszeg(n):
    if n==0:
        return 0
    return n+rekurziv_osszeg(n-1)

def fibonacci(n):
    if n<3:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def szamjegy(a):
    if a==0:
        return 0
    return a%10+szamjegy(a//10)

def max_keres(lista):
    if len(lista)==1:
        return lista[0]
    return max(lista[0],max_keres(lista[1:]))

def szam_fordit(x,forditott):
    if x==0:
        return forditott
    return szam_fordit(x//10,forditott*10+x%10)

def string_fordit(szo):
    if szo=="":
        return szo
    return string_fordit(szo[1:])+szo[0]

def lnko(a,b):
    if a%b==0:
        return b
    return lnko(b,a%b)



n=int(input("Adj meg egy szamot:"))
print("Faktorialis:",factorial(n))
print("Szamjegyek osszege:",rekurziv_osszeg(n))
print("Foibonacci:",fibonacci(n))
a=int(input("Adj meg egy tobb szamjegyu szamot:"))
print("Tobb szamjegyu szam szamjegyeinek osszege:",szamjegy(a))

lista=[random.randint(1,100) for i in range(10)]
print("Lista:",lista)
print("Max elem:",max_keres(lista))

x=int(input("Adj meg egy szamot:"))
print(szam_fordit(x,0))

szo=input("Szo:")
print("Forditott szo:",string_fordit(szo))

a,b=int(input("a:")),int(input("b:"))
print(lnko(a,b))