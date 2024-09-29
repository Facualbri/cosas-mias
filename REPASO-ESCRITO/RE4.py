#Se dispone de diez pares ordenados (X,y) de números. a los cuales se debe calcular la suma
# de todas las X y la suma de todas las Y, imprimir los resultados.

x=0
y=0
sumax=0
sumay=0

for i in range(0, 10):
    x=int(input("ingrese un valor de x: "))
    y=int(input("ingrese un valor de y: "))
    sumax=sumax+x
    sumay=sumay+y
    print(f"la suma de todas las x es de {sumax} y la suma de las y es de {sumay}")