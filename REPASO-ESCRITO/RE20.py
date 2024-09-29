#Ingresar de a uno, una serie de números. Encontrar e imprimir el mayor de todos los números
# pares cuyo número de orden sea par, el proceso terminará cuando el número lerdo sea
# igual a cero.

# Inicializar variables
mayor_par = None  # Almacena el mayor número par
contador = 0  # Contador para el orden de los números ingresados

while True:
    # Pedir al usuario que ingrese un número
    numero = int(input("Ingrese un número (0 para terminar): "))
    
    # Terminar el proceso si se ingresa 0
    if numero == 0:
        break
    
    contador += 1  # Incrementar el contador

    # Verificar si el número es par y su orden es par
    if numero % 2 == 0 and contador % 2 == 0:
        # Si es el primer número par encontrado o es mayor que el actual mayor_par
        if mayor_par is None or numero > mayor_par:
            mayor_par = numero  # Actualizar el mayor par

# Imprimir el resultado
if mayor_par is not None:
    print(f"El mayor número par en posición par ingresado es: {mayor_par}")
else:
    print("No se ingresaron números pares en posiciones pares.")

# Imprimir el resultado
print(f"El mayor número ingresado es: {mayor_par}")

