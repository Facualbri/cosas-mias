#Para elaborar la misma estadística, se necesita verificar que todos los valores ingresados sean
# mayor ó igual que cero; En caso contrario indicar que se trata de un error; ignorar el dato
# leído y leer el próximo

mayor_valor = 0  

while True:
    try:
        numero = int(input("Ingrese un número de sorteo (o un número mayor que 999 para terminar): "))
    
        if numero<=0:
            print("Error: El número debe ser mayor o igual a cero. Intente de nuevo.")
            continue

        if numero > 999:
            break  
        
        if numero > mayor_valor:
            mayor_valor = numero 
    
    except ValueError:
        print("se trata de un error al ingrese un numero menor a 0")
    
print(f"El mayor valor registrado en los sorteos es: {mayor_valor}")
