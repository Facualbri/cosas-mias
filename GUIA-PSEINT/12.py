gananciadiraria=float(input("ingrese la ganancia diaria: "))
promediopuntos=float(input("ingrese el promedio de puntos que tienes: "))
dineroperdido=float(input("ingrese el dinero perdido: "))
dias1=int(input("ingrese los puntos del dia lunes: "))
dias2=int(input("ingrese los puntos del dia martes: "))
dias3=int(input("ingrese los puntos del dia miercoles: "))
dias4=int(input("ingrese los puntos del dia jueves: "))
dias5=int(input("ingrese los puntos del dia viernes: "))

print(f"dia 1. {dias1} ")
print(f"dia 2. {dias2} ")
print(f"dia 3. {dias3} ")
print(f"dia 4. {dias4} ")
print(f"dia 5. {dias5} ")

gananciat= dias5 + dias1 + dias2 + dias3 + dias4
print(f"la ganancia total es de {gananciat}")

promediop= gananciat / 5
if promediop > 170:
    dineroperdido= (0.5*gananciat*5) + (gananciat*5)
else:
    dineroperdido=0

print(f"Obtuviste un promedio de {promediop} puntos IMECA")
print(f"dinero perdido: {dineroperdido}")



