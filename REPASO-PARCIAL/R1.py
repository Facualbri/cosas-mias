import math

numeroentero=int(input("ingrese un numero entero: "))
numerodigitos=int()

if numeroentero == 0:
    numerodigitos=1
    print(f"la cantidad de digitos es de {numerodigitos} ")
else:
    numerodigitos=0
    while numeroentero != 0:
        numeroentero=math.trunc(numeroentero/10)
        numerodigitos = numerodigitos +1
        print(f"la cantidad de digitos es de {numerodigitos}")

      
