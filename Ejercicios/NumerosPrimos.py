#NumerosPrimos
nro=input("Ingrese un numero:")
if (nro.isdigit()):
    nro=int(nro) #Convertir la entrada de tipo TEXTO "3" a numero 3
    div=2
    band= True #Boolean para comprobar si el numero es primo o no
    if nro ==1:
        print("Es primo")
    else:
        while band and (nro>div):  #band ==True equivalente band
            if nro % div == 0:
                band = False
                break
            #Finsi
            div += 1 #div = div +1
        #FinMientras
        if band:  #band ==True equivalente band
            print("Es primo")
        else:
            print("No es primo")
        #Finsi
    #Finsi
else:
    print('Por favor entre un numero valido')