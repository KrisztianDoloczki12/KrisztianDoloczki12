#buborek_rendezes
a=[7,3,9,2,6]
n=len(a)
regibal=1
regijobb=n-1
rendben=False
while not rendben:
    print("elso kor")
    rendben=True
    jobb=0
    for i in range(regibal,regijobb):
        if a[i]>a[i+1]:
            rendben=False
            id=a[i]
            a[i]=a[i+1]
            a[i+1]=id
            if i>jobb:
                jobb=i
            print("jobb:",jobb)
    if not rendben:
        regijobb=jobb
        bal=n
        for i in range(regijobb,regibal):
            if a[i]>a[i+1]:
                rendben=False
                id=a[i]
                a[i]=a[i+1]
                a[i+1]=id
                if i<bal:
                    bal=i
                print("bal:",bal)
        regibal=bal
print("Rendezett lista:",a)