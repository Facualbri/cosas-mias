import math 

num1=float(input("ingrse un numero: "))
num2=float(input("ingrse un numero: "))
num3=float(input("ingrse un numero: "))

if num1 == 1:
    suma=num2 + num3
    print(f"la suma de {num2} y {num3} es {suma}")
elif num1 == 2:
    multiplicacion=num2 * num3
    print(f"la multiplicacion de {num2} y {num3} es {multiplicacion}")
elif num1 == 3:
    division=num2 / num3
    print(f"la division de {num2} y {num3} es {division}")
elif num1 == 4:
    cuadrado2=num2 * num2
    cuadrado3=num3 * num3
    suma_cuadrados= cuadrado2 + cuadrado3
    raiz= math.sqrt(suma_cuadrados)
    print(f"la raiz cuadrada de la suma de los cuadrados es de {num2} y {num3} es {raiz}")
    
