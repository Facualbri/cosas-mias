horas = int(input("Horas: "))
minutos = int(input("Minutos: "))

# Si hay minutos, se considera una hora mas
if minutos >= 1:
    horas += 1

total = horas * 2

print(f"Se debe pagar al estacionamiento ${total}")