#Divisores_de_numero
while(True):
    #solo vale para numeros enteros
    print("Ingrese Numero entero,(N para salir):")
    Num=input()
    if(Num.isdigit()):
        #Num=int(Num)
        Num=float(Num)
        div=1
        while(div<=Num):
            if(Num%div == 0):
                print(div)
            #Fin si
            #div=div+1
            div+=1
        #Din while
    else:
        if(Num=="N"):
            break
        print("Por favor entre un numero valido")

#Fin Divisores_de_numero
