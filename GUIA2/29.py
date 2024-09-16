import math

num1=float(input("ingrse un numero: "))
num2=float(input("ingrse un numero: "))
num3=float(input("ingrse un numero: "))

suma1=num1+num2+num3

if suma1 > 10:
    suma2=math.sqrt(suma1)
    print(f"la raiz cuadrada es {suma2}")
else:
    num4=float(input("ingrse un numero: "))
    num5=float(input("ingrse un numero: "))
    suma3=suma1 + num4 + num5
    print(f"la suma es de {suma3}")

    