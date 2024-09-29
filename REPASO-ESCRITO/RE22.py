# Se dispone de una serie de ternas de números enteros positivos y se quiere calcular e
# imprimir la suma de cada una de ellas, indicando mediante un mensaje si dicha suma es
# Par. Fin de proceso cuando alguna suma sea mayor que setecientos.

while True:
    # Pedir al usuario que ingrese tres números enteros positivos
    a = int(input("Ingrese el primer número (positivo): "))
    b = int(input("Ingrese el segundo número (positivo): "))
    c = int(input("Ingrese el tercer número (positivo): "))

    # Calcular la suma
    suma = a + b + c

    # Imprimir la suma
    print(f"La suma de {a}, {b} y {c} es: {suma}")

    # Verificar si la suma es par
    if suma % 2 == 0:
        print("La suma es par.")
    else:
        print("La suma es impar.")

    # Terminar el proceso si la suma es mayor que 700
    if suma > 700:
        print("La suma es mayor que 700. Fin del proceso.")
        break
