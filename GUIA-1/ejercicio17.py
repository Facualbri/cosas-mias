import math 

radiocm=50
distanciakm=1

radiom=radiocm / 100
distanciam=distanciakm * 1000
circunferencia = 2 * math.pi * radiom
vueltas=distanciam / circunferencia

print(f"cada rueda dara aprox {vueltas} para recorrer un km")