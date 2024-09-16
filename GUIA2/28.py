num1=float(input("ingrese un numero1: "))
num2=float(input("ingrese un numero2: "))
num3=float(input("ingrese un numero3: "))

if num1 < num2 > num3:
    print(f"el numero {num2} es mayor")
elif num2 < num1 > num3:
    print(f"el numero {num1} es el mayor")
elif num1 < num3 > num2:
     print(f"el numero {num3} es mayor")
else:
    print("los numeros son iguales")
