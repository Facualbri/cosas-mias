import math

# Pedir al usuario la base, la altura y el ángulo
base = float(input("Introduce la longitud de la base del triángulo: "))
altura = float(input("Introduce la altura del triángulo: "))
angulo_base = float(input("Introduce el ángulo (en grados) que forma la base con el cateto opuesto: "))

# Calcular la superficie del triángulo
superficie = 0.5 * base * altura
print(f"La superficie del triángulo es: {superficie:}")

# Convertir el ángulo de grados a radianes
angulo_base_rad = math.radians(angulo_base)

# Calcular los otros dos lados
cateto_opuesto = base * math.tan(angulo_base_rad)
hipotenusa = base / math.cos(angulo_base_rad)

print(f"Longitud del cateto opuesto: {cateto_opuesto}")
print(f"Longitud de la hipotenusa: {hipotenusa}")