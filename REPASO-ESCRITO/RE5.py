#se debe calcular e imprimir el producto de todas las X Y de todas las y de cincuenta pares
#ordenados de números enteros.

producto = 1

for i in range(50):
    X = int(input("Ingrese el valor de X: "))
    Y = int(input("Ingrese el valor de Y: "))
    productoX = producto * X
    productoY = producto * Y
    print(f"El producto de todos los pares (X) es: {productoX}")
    print(f"El producto de todos los pares (Y) es: {productoY}")
