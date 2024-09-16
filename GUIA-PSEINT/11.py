import random

total = float(input("Total de compra: "))

numero_azar = random.randint(0, 99)

print(f"Sacaste el número... ¡{numero_azar}! ")

if numero_azar < 74:
    print("Descuento del 15%")
    porcentaje_descuento = 0.15
else:
    print("Descuento del 20%")
    porcentaje_descuento = 0.20

# el monto del descuento
descuento = total * porcentaje_descuento

#total final después del descuento
total_final = total - descuento

print(f"El descuento será de ${descuento}")
print(f"El total final será de ${total_final}")

