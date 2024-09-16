numero = int(input("Ingrese un número entero positivo menor que 100: "))

es_primo = 1 

if 0 < numero < 100:
    if numero < 2:
        es_primo = 0  # No es primo
    elif numero in (2, 3, 5, 7):
        es_primo = 1  # Es primo
    elif numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
        es_primo = 0  # No es primo
    else:
        es_primo = 1  # Es primo
    
    if es_primo == 1:
        print(f"{numero} es primo.")
    else:
        print(f"{numero} no es primo.")
else:
    print("El número ingresado debe ser positivo y menor que 100.")

    #REVISAR DESPUES