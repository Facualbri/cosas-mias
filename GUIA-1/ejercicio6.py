largo=float(input("ingrese el largo de la pared: "))
altura=float(input("ingrese la altura de la pared: "))
paredp=3.6
pintura=paredp * 2 

area=altura * largo
lnecesarios=area - pintura

print(f"necesitas apoximadamente {lnecesarios}L de pintura")
