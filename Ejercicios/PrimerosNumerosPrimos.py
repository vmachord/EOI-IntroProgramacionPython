#NumerosPrimos
numeroDePrimos=input("Ingrese un numero:")
if (numeroDePrimos.isdigit()):
    numeroDePrimos=int(numeroDePrimos) #Convertir la entrada de tipo TEXTO "3" a numero 3
    #iteracion
    #for numerosPrimos in range(1,nro+1): # numerosPrimos = 1 hasta numerosPrimos>(nro+1) y paso 1
                                         # For no es util aqui porque no mostraria los N numeros primos
                                         # Contador=1 hasta que Contador == numerosDePrimos cada primo suma Contador HAGA
                                         # Mientras que numeroDePrimos > 0 (cada primo restaNumeroDePrimos)
    nro=1                                #nro es para el while el for lo inicia automaticamente
    while numeroDePrimos>0 :    
        div=2
        band= True #Boolean para comprobar si el numero es primo o no
        if nro ==1:
            print(f" {nro} es primo")
            numeroDePrimos-=1
        else:
            while band and (nro>div):  #band ==True equivalente band
                if nro % div == 0:
                    band = False
                    break
                #Finsi
                div += 1 #div = div +1
            #FinMientras
            if band:  #band ==True equivalente band
                print(f"{nro} es primo")
                numeroDePrimos-=1
            #else:
            #    print("No es primo")
            #Finsi
        #Finsi
        nro+=1
else:
    print('Por favor entre un numero valido')