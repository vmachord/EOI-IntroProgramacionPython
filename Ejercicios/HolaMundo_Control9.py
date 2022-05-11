# Hola Mundo
print("Hola mundo")

# Control Numero 9

N=0
print("Escribir el numero")
N=input() #input te da valor tipo texto, por eso lo convertis a int
if(N.isdigit()):
    N=int(N)
    if (N==9): #si es capaz de comparar string con numero
        print("El numero es igual a 9")
    else: 
        if(N>9):
            print("El numero es mayor a 9")
        else:
            print("El numero es menor a 9")
        #Fin si
    #Fin Si
else:
    print("Por favor entre un valor numerico")
#Fin Control Numero 9