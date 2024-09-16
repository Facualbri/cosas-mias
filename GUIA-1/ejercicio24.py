
km=float(input("ingrese la cantidad de km recorridos: "))
precioc=float(input("coloque el precio del combustible: "))
kms=float(input("km recorridos por cada litro: "))

litrosconsumido=km / kms
importegastado=litrosconsumido * precioc

print(f"la cantidad de litros consumidos fueron {litrosconsumido}L")
print(f"el total de gastos en combustible es de ${importegastado}")

