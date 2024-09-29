#Leer por teclado una serie de valores, imprimiendo para cada valor su raíz cuadrada si es par
# y su cuadrado si es impar. Ultimo valor, cero (no debe ser procesado).

import math

numero=1

while numero>0:
    numero=int(input("ingrese un numero: "))
    
    if numero % 2 == 0:
        raiz=math.sqrt(numero)
        print(f"el numero ingresado es par, por la tanto su raiz es {raiz}")
    else:
        cuadrado=numero*numero
        print(f"el numero ingresado es impar, por la tanto su cuadrado es {cuadrado}")