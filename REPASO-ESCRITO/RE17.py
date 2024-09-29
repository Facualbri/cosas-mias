#Leer un número y si es múltiplo de cuatro sin serlo de cinco, calcular los diez primeros
# múltiplos de dicho número, sino su mitad, tercera y cuarta parte, imprimiendo los valores
# mientras se calculan.

numero=int(input("ingrese un numero: "))

for i in range(1,11):
    if numero % 4 == 0 and numero % 5 != 0:
        multiplos=numero*i
        print(f"{i} multiplo de {numero} son {multiplos}")
    
if numero % 4 == 0 and numero % 5 == 0:
    mitad=numero/2
    tercera=numero/3
    cuarta=numero/4
    print(f"la mitad de {numero} es {mitad}")
    print(f"la tercera  parte de {numero} es {tercera}")
    print(f"cuarta parte de {numero} es {cuarta}")