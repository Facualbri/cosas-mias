#Leer una serie de cincuenta números enteros. Informar cuantos son mayores que 100.
contador=0
for i in range(50):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    if numero > 100:
        contador= contador +1
        print(f"hay {contador} de numeros mayores a 100")
    
