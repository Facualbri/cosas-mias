n=int(input("escribe el valor de n: "))
i=int()
suma=0

for i in range(1, n+1):
    numeroingresado=int(input("ingrese un numero: "))
    suma=suma + numeroingresado

print(f"el resultado de la suma es de: {suma}")