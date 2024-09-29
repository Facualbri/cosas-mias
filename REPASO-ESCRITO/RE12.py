#Ídem al problema anterior, pero esta vez, el fin del proceso está dado cuando el importe
#mayor supere los mil.

codigo_mayor = 0
importe_mayor = -1 
codigo_menor = 0
importe_menor = float('inf') 

while True:
    codigo_vendedor = int(input("Ingrese el código del vendedor (0 para terminar): "))

    if codigo_vendedor == 0:
        break
    
    importe = float(input("Ingrese el importe de la venta: "))
    
    if importe == 0:
        break

    if importe > importe_mayor:
        importe_mayor = importe
        codigo_mayor = codigo_vendedor
    
    if importe_mayor==1000:
        print("finalizo el programa por superar los 1000 como mayor valor")
        break

    if importe < importe_menor:
        importe_menor = importe
        codigo_menor = codigo_vendedor

if codigo_mayor != 0:
    print(f"El vendedor con mayor venta es el código {codigo_mayor} con un importe de {importe_mayor}.")
if codigo_menor != 0:
    print(f"El vendedor con menor venta es el código {codigo_menor} con un importe de {importe_menor}.")
if codigo_mayor == 0 and codigo_menor == 0:
    print("No se registraron ventas.")