#En un comercio hay cuatro vendedores y quieren saber, cuál fue el que realizó la venta de
# mayor importe, y cual la venta de menor importe. Terminar el proceso cuando el importe
# leído sea cero. los datos se leerán de a pares (Codven, Imp).

codigo_mayor = 0
importe_mayor = -1  # Comenzamos con un número negativo para asegurarnos de que cualquier importe válido sea mayor
codigo_menor = 0
importe_menor = float('inf')  # Comenzamos con un número muy alto

while True:
    # Leer el código del vendedor
    codigo_vendedor = int(input("Ingrese el código del vendedor (0 para terminar): "))
    
    # Terminar el proceso si se ingresa 0 como código
    if codigo_vendedor == 0:
        break
    
    # Leer el importe de la venta
    importe = float(input("Ingrese el importe de la venta: "))
    
    # Verificar si el importe es cero para terminar
    if importe == 0:
        break
    
    # Actualizamos el mayor importe y el vendedor correspondiente
    if importe > importe_mayor:
        importe_mayor = importe
        codigo_mayor = codigo_vendedor
    
    # Actualizamos el menor importe y el vendedor correspondiente
    if importe < importe_menor:
        importe_menor = importe
        codigo_menor = codigo_vendedor

if codigo_mayor != 0:
    print(f"El vendedor con mayor venta es el código {codigo_mayor} con un importe de {importe_mayor}.")
if codigo_menor != 0:
    print(f"El vendedor con menor venta es el código {codigo_menor} con un importe de {importe_menor}.")
if codigo_mayor == 0 and codigo_menor == 0:
    print("No se registraron ventas.")