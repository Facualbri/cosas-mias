numero_verificar = int(input("Ingrese el número: "))
divisores = 0


for i in range(2, numero_verificar): 
    if numero_verificar % i == 0:
        divisores = divisores + 1

print("Cantidad de divisores:", divisores)


if divisores > 0:
    print("NO ES PRIMO")
else:
    print("ES PRIMO")