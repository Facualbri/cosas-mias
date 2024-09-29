#En una serie de treinta y cuatro elementos, se quiere calcular e imprimir el cuadrado de cada
# número, deberán ser leído dos uno por vez.

for i in range(34):
    numeros=int(input("ingrese un numero para saber su cuadrado: "))
    cuadrado= numeros*numeros*numeros
    print(f"el cuadrado de {numeros} es de: {cuadrado}")
