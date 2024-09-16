import math

lado = float(input("Introduce la longitud de un lado del triángulo rectángulo: "))
hipotenusa = float(input("Introduce la longitud de la hipotenusa: "))

# Calcular el lado restante usando el teorema de Pitágoras
lado_restante = math.sqrt(hipotenusa**2 - lado**2)

# Calcular la superficie del triángulo
superficie = 0.5 * lado * lado_restante

# Calcular los ángulos en radianes
angulo_lado_rad = math.asin(lado / hipotenusa)
angulo_lado_deg = math.degrees(angulo_lado_rad)
angulo_restante_deg = 90 - angulo_lado_deg

print(f"Longitud del lado restante: {lado_restante}")
print(f"Superficie del triángulo: {superficie}")
print(f"Ángulo adyacente al lado ingresado: {angulo_lado_deg} grados")
print(f"Ángulo restante: {angulo_restante_deg} grados")
