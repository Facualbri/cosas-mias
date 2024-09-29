#Ingresar por teclado de a uno una serie de números. Encontrar e imprimir el menor de los
# números pares. La cantidad de elementos leídos es cien.

numero=1
i=0
menor_par= None

for i in range(100):
    numero=int(input("ingrese un numero: "))

    if numero % 2 == 0:
        if menor_par is None or numero < menor_par:
            menor_par = numero

if menor_par is not None:
    print(f"El menor número par ingresado es: {menor_par}")
else:
    print("No se ingresaron números pares.")
