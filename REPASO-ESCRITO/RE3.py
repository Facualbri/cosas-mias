#Leer una serie de números enteros. que contenga como máximo veinte elementos, en caso de
# ingresar un valor negativo o la cantidad de números ingresados supere los veinte, detener
# el proceso e informar mediante un mensaje cuántos son mayores que 100.

contador=0 
for i in range(50):
    numeroingresado=int(input(f"ingrese un numero {i + 1}: "))
    if numeroingresado<0:
        print("el proceso a finalizado ya que ingresaste un numero negativo")
        break
    elif numeroingresado>100:
        contador=contador+1
        print(f"hay {contador} de numeros mayores a 100")