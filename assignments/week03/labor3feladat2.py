import math

orak=float(input("Kerem adja meg, hogy hany orat parkolt:"))
orak=math.ceil(orak)
dij=3+2*(orak-1)
print("Parkolasi dij:",dij)