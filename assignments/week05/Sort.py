def bubble_sort(a):
    n=len(a)
    while n>1:
        uj_n=0
        for i in range(1, n):
            if a[i-1]>a[i]:
                a[i-1],a[i]=a[i],a[i - 1]
                uj_n=i
        n=uj_n
        if n==0:
            break
    return a

a=[7,3,9,2,6]
print("Rendezetlen tomb:",a)
rendezett_tomb=bubble_sort(a)
print("Rendezett tomb optimalizalt bubble sorttal:",rendezett_tomb)

def selection_sort(a):
    n=len(a)
    for i in range(0,n-1):
        min_index=i
        for j in range(i+1,n):
            if a[j]<a[min_index]:
                min_index=j
        a[i],a[min_index]=a[min_index],a[i]
    return a

a=[8,4,5,2,9]
print("\nRendezetlen tomb:",a)
rendezett_tomb=selection_sort(a)
print("Rendezett tomb kivalasztasos rendezessel:",rendezett_tomb)

def insertion_sort(a):
    n=len(a)
    for j in range(1,n):
        seged=a[j]
        i=j-1
        while i>=0 and a[i]>seged:
            a[i+1]=a[i]
            i-=1
        a[i+1] = seged
    return a


a=[6,3,8,2,7]
print("\nRendezetlen tomb:",a)
rendezett_tomb=insertion_sort(a)
print("Rendezett tomb beszurasos rendezessel:",rendezett_tomb)

def sort(a):
    n=len(a)
    rendben=False
    while rendben==False:
        rendben=True
        for i in range(0,n-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                rendben=False

    for i in range(0,n-1):
        minindex=i
        for j in range(i+1,n):
            if a[minindex]>a[j]:
                minindex=j
        a[i],a[minindex]=a[minindex],a[i]
    return a

a=[6,4,85,0,36]
print("\nRendezetlen tomb:",a)
rendezett_tomb=sort(a)
print("Rendezett tomb buborekos/kivalasztasos mix rendezessel:",rendezett_tomb)