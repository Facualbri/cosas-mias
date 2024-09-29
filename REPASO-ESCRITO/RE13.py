#Leer un número calcular la raíz cúbica y así sucesivamente hasta que el resultado sea menor
# o igual qué uno, imprimir los resultados parciales y finales. Controlar que el número leido
# sea mayor que cero al comenzar el proceso.

import math

numero=int(input("ignrese un numero para saber su raiz cubica: "))

if numero >= 0:
    print("hay un error ya que el numero no es mayor que cero")
else:
    print(f"el numero inicial fue {numero}")

while numero > 1:
    numero=math.pow(numero, 1/3)
    print(f"la raiz cubica es de {numero}")

print(f"el resultado final es {numero}")