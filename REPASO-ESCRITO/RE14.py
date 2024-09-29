#En un instituto de enseñanza, se quiere emitir un listado de todos aquellos alumnos que el
# promedio general sea superior a siete, para lo cual se ingresa como dato: número de legajo
# y los promedios de las cuatro materias que se dictan. Terminar el proceso cuando se lea
# un número de legajo igual a cero.

numero_legajo=1
promedios=float
promediog=float

while numero_legajo>0:
    print("ingrese el numero de legajo del alumno, para salir del programa coloque el cero")
    numero_legajo=int(input("numero de legajo: "))
    i=0
    
    if numero_legajo==0:
        print("usted a salido del programa")
        break
    else:
        for i in range(1): 
            promedios0=float(input(f"ingrese el promedio de las cuatro materias para sacar un promedio general: "))
            promedios1=float(input(f"ingrese el promedio de las cuatro materias para sacar un promedio general: "))
            promedios2=float(input(f"ingrese el promedio de las cuatro materias para sacar un promedio general: "))
            promedios3=float(input(f"ingrese el promedio de las cuatro materias para sacar un promedio general: "))

            promedios=promedios0+promedios1+promedios2+promedios3
            promediog=promedios/4
    print(f"el promedio general del alumno {numero_legajo} es de {promediog}")
        


    

   