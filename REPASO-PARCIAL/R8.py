numeroingresado=1
positivos=0
negativos=0
neutros=0
n=int(input("ingrese el valor de n: "))

for i in range(1, n+1):
    numeroingresado=int(input("ingrese un numero: "))
    if numeroingresado > 0:
        positivos=positivos +1
    elif numeroingresado<0:
        negativos=negativos +1
    else:
        neutros=neutros+1

print(f"positivos: {positivos}")
print(f"negativos: {negativos}")
print(f"neutros: {neutros}")
