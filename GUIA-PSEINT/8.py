a = float(input("Ingrese el valor de A: "))
b = float(input("Ingrese el valor de B: "))
print("ELIJA UNA OPCIÓN")
print("[1] Suma")
print("[2] Resta")
print("[3] Multiplicación")
print("[4] División")
op = int(input("Ingrese la opción (1, 2, 3, o 4): "))

# Realizamos la operación seleccionada
if op == 1:
    resultado = a + b
    print(f"La suma es {resultado}")
else:
    if op == 2:
        resultado = a - b
        print(f"La resta es {resultado}")
    else:
        if op == 3:
            resultado = a * b
            print(f"La multiplicación es {resultado}")
        else:
            if op == 4:
                if b != 0:  # Comprobamos si el divisor es diferente de 0
                    resultado = a / b
                    print(f"La división es {resultado}")
                else:
                    print("Error: División por cero no permitida")
            else:
                print("Operación inválida")