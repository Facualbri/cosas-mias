#En una oficina meteorológica se dispone de las temperaturas máximas y mínimas diarias, a
# lo largo de un período x. Se quieren encontrar las temperaturas mínima, máxima, la
# máxima de las mínimas y la mínima de las máximas. Se debe ingresar los datos de a pares
# ordenados (mín, max). El proceso termina cuando las temperaturas leídas sean (noventa y
# nueve - noventa y nueve).

periodo=int(input("ingrese el periodo para saber las temperaturas: "))
tempmax=0
tempmin=0
minima=tempmin
maxima=tempmax
minmax=tempmax
maxmin=tempmin
i=0
while i <= periodo:
    tempmax=float(input("ingrese el valor de la temperatura maxima: "))
    tempmin=float(input("ingrese el valor de la temperatura minima: "))
    if tempmax == 99 and tempmin ==99:
        i=periodo+1
    else:
        if minima>tempmin:
            minima=tempmin
        if maxima<tempmax:
            maxima=tempmax
        if maxmin>tempmin:
            maxmin=tempmin
        if minmax<tempmax:
            minmax=tempmax

print(f"la temperatura maxima es {tempmax}")
print(f"la temperatura manima es {tempmin}")
print(f"la temperatura maxima de las minimas es {maxmin}")
print(f"la temperatura minima de las maxima es {minmax}")