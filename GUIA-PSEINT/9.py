costo_individual = 9000
cantidad = int(input("Ingrese la cantidad de computadoras compradas: "))
descuento = 0

if 10 < cantidad < 20:
    descuento = 0.10  # 10%
else:
    if 20 <= cantidad < 50:
        descuento = 0.15  # 15%
    else:
        if cantidad >= 50:
            descuento = 0.25  # 25%

total = cantidad * costo_individual

total -= total * descuento

print(f"El total a pagar sería ${total}")
