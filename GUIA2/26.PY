import math

num1=float(input("ingrese un numero: "))
num2=float(input("ingrese un numero: "))
num3=float(input("ingrese un numero: "))

if num2 < 0: 
    suma = num1 + num2
    raiz= math.sqrt(suma)
    print(f"la suma es {suma} y la raiz de la misma es {raiz}")
else:
    print("ERROR")
