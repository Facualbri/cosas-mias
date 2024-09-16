import math

cateto1 = float(input("Introduce la longitud del primer cateto: "))
cateto2 = float(input("Introduce la longitud del segundo cateto: "))
   
#teorema de Pitágoras: hipotenusa^2 = cateto1^2 + cateto2^2
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print(f"La longitud de la hipotenusa es: {hipotenusa:.2f}")