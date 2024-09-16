mes=int(input("ingrese el numero del mes: "))
dia=int(input("ingrese el numero del dia: "))

print(f"el dia es {dia}")
print(f"el mes es {mes}")

if mes >= 1 and mes <= 12: 
    if dia <= 0:
        print("es incorrecto")
    elif mes == 1:
        # Enero
        if 1 <= dia <= 31:
            print("Correcto")
        else:
            print("Incorrecto")
    elif mes == 2:
        #febrero
        if 1<= dia <=29:
            print("correcto") 
        else:
            print("incorrecto")
    elif mes == 3: 
        #marzo
        if 1<= dia <=31:
            print("correcto")
        else:
            print("incorrecto")        
    elif mes == 4: 
        #abril
        if 1<= dia <=30:
            print("correcto")
        else:
            print("incorrecto")
    elif mes == 5: 
        #mayo
        if 1<= dia <=30:
            print("correcto")
        else:
            print("incorrecto")    
    elif mes == 6: 
        #junio
        if 1<= dia <=30:
            print("correcto")
        else:
            print("incorrecto")
    elif mes == 7: 
        #julio
        if 1<= dia <=31:
            print("correcto")
        else:
            print("incorrecto")
    elif mes == 8: 
        #agosto
        if 1<= dia <=31:
            print("correcto")
        else:
            print("incorrecto")
    elif mes == 9: 
        #septiembre
        if 1<= dia <=30:
            print("correcto")
        else:
            print("incorrecto")
    elif mes == 10: 
        #octubre
        if 1<= dia <=30:
            print("correcto")
        else:
            print("incorrecto")
    elif mes == 11: 
        #noviembre
        if 1<= dia <=30:
            print("correcto")
        else:
            print("incorrecto")
    elif mes == 12: 
        #diciembre
        if 1<= dia <=31:
            print("correcto")
        else:
            print("incorrecto")
else:
     print("Incorrecto")