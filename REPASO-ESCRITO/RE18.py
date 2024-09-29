#Ingresando un número como dato, imprimir de sus primeros cincuenta múltiplos, que no
# sean a la vez múltiples de seis.

numero=int(input("ingrese un numero: "))

for i in range(1,51):
    if numero % numero== 0 and numero % 10 != 0:
        multiplos=numero*i
        print(f"{i} multiplo de {numero} son {multiplos}")

if numero % numero== 0 and numero % 10 == 0:
    print("a colocado un multipo de 10, por lo tanto no se hara la operacion")