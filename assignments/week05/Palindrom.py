szo=input("Szo:")
palindrom=True
for i in range(len(szo)):
    if szo[i]!=szo[-(i+1)]:
        palindrom=False
        break

if palindrom:
    print(szo,"palindrom")
else:
    print(szo,"nem palindrom")
