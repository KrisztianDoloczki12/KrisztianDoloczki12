eredmenyek = [45, 78, 90, 32, 67, 50, 98, 44]
sum=0
sikeres=0
elegtelen=False
for i in range(0,len(eredmenyek)):
    if i==0:
        max=eredmenyek[i]
    sum+=eredmenyek[i]
    if eredmenyek[i]>max:
         max=eredmenyek[i]
    if eredmenyek[i]>50:
        sikeres+=1
    if eredmenyek[i]<50:
       elegtelen=True
atlag=sum/len(eredmenyek)
if elegtelen==True:
    print("Letezik elegtelen eredmeny")
print("atlag:",atlag)
print("sikeres:",sikeres)
print("legjobb eredmeny",max)