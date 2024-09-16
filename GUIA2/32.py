sueldo=float(input("ingrese su sueldo mensual: "))
categoria=int(input("ingrese su catagoria en numero: "))


if categoria == 1:
    descuento = sueldo * 0.30
    descuentof= sueldo - descuento
    print(f"el descuento es de 30% y su total es de {descuentof}")
elif categoria == 2:
    descuento = sueldo * 0.25
    descuentof= sueldo - descuento
    print(f"el descuento es de 25% y su total es de {descuentof}")
elif categoria == 3:
    descuento = sueldo * 0.25
    descuentof= sueldo - descuento
    print(f"el descuento es de 25% y su total es de {descuentof}")
elif categoria == 4:
    descuento = sueldo * 0.10
    descuentof= sueldo - descuento
    print(f"el descuento es de 10% y su total es de {descuentof}")
else:
    print("para otras categorias no se encuentran descuentos")

    
