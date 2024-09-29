#Leer de a uno, una serie de números enteros, e imprimir un “*” al lado de cada número par.
# El proceso termina cuando el número leído sea cero.

numero=1

while numero>0:
    
    if numero == 0:
        print("usted a salido del programa")
        break
    else:
        numero=int(input("ingrese un numero entero: "))
        if numero % 2 == 0:
            print(f"{numero}*")
            continue

    
