def calcular_velocidad():
    velocidad=distancia_recorrida/tiempo_empleado
    return velocidad

distancia_recorrida=float(input("Ingrese la distancia recorrida (km): "))
tiempo_empleado=float(input("Ingrese el tiempo que tardo que recorrer cierta distancia(h): "))

velocidad=calcular_velocidad()
print(f"El vehiculo se desplaza a una velocidad de {velocidad}km/h.")