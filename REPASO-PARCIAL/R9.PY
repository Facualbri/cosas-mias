n=int(input("ingrese la cantidad de notas: "))

promedio=0
for i in range(0, n):
    nota=int(input(f"ingrese la nota numero {i}: "))
    if nota >= 0 and nota <=10:
        promedio= promedio + nota
    else:
        i=int(input(f"nota incorrecta, escribela nuevamente: "))
        i=i-1

promedio=promedio/n
print(f"el promedio de notas del alumno es de {promedio}")

