#Ingresar de a uno una serie de números. Encontrar e Imprimir el mayor de todos los números
# pares, el proceso terminará cuando el número leído sea igual a cero.

mayor_par = None

while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    if numero % 2 == 0 and (mayor_par is None or numero > mayor_par):
        mayor_par = numero

if mayor_par is not None:
    print(f"El mayor número par ingresado es: {mayor_par}")
else:
    print("No se ingresaron números pares.")
        