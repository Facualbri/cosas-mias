#Para poder extraer alguna estadística, en una agencia de quiniela, se requiere saber cuál fue
# el mayor valor registrado en los sorteos comprendidos en un periodo de tiempo
# determinado, Terminar el proceso de carga de los números, cuando el valor leído sea
# mayor que novecientos noventa y nueve.

mayor_valor = 0  

while True:
    numero = int(input("Ingrese un número de sorteo (o un número mayor que 999 para terminar): "))
    if numero > 999:
        break  
    if numero > mayor_valor:
        mayor_valor = numero 

print(f"El mayor valor registrado en los sorteos es: {mayor_valor}")

