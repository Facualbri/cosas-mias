#21. Ingresar por teclado los precios correspondientes a cinco artículos y las cantidades vendidas de cada uno de ellos. 
# Calcular e imprimir el importe total de ventas de cada uno y un importe total de lo vendido.

producto1= str(input("ingrese un articulo: "))
producto2= str(input("ingrese un articulo: "))
producto3= str(input("ingrese un articulo: "))
producto4= str(input("ingrese un articulo: "))
producto5= str(input("ingrese un articulo: "))

precio1= float(input(f"ingrese el precio de {producto1}: "))
precio2= float(input(f"ingrese el precio de {producto2}: "))
precio3= float(input(f"ingrese el precio de {producto3}: "))
precio4= float(input(f"ingrese el precio de {producto4}: "))
precio5= float(input(f"ingrese el precio de {producto5}: "))

cantidad1= int(input(f"ingrese la cantidad vendida de {producto1}"))
cantidad2= int(input(f"ingrese la cantidad vendida de {producto2}"))
cantidad3= int(input(f"ingrese la cantidad vendida de {producto3}"))
cantidad4= int(input(f"ingrese la cantidad vendida de {producto4}"))
cantidad5= int(input(f"ingrese la cantidad vendida de {producto5}"))

importet1= precio1 * cantidad1
importet2= precio2 * cantidad2
importet3= precio3 * cantidad3
importet4= precio4 * cantidad4
importet5= precio5 * cantidad5

totalv1= importet1
totalv2= importet2
totalv3= importet3
totalv4= importet4
totalv5= importet5

print(f"el total vendido es de {totalv1}")
print(f"el total vendido es de {totalv2}")
print(f"el total vendido es de {totalv3}")
print(f"el total vendido es de {totalv4}")
print(f"el total vendido es de {totalv5}")

print(f"el importe total es de {importet1}")
print(f"el importe total es de {importet2}")
print(f"el importe total es de {importet3}")
print(f"el importe total es de {importet4}")
print(f"el importe total es de {importet5}")