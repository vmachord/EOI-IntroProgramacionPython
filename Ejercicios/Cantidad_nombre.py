#Cantidad_nombre
nombre=input("Ingresar Nombre:")
num=input("Ingresar Cantidad:")
if(not nombre.isdigit()):
    if(num.isdigit()):
        num=int(num)
        print((f"{nombre}\n")*int(num))
        #while(num>0):
        #    print(nombre)
        #    num=num - 1
    else:
        print("Por favor entre una cantidad numerica")
else:
    print("Por favor entre el nombre en texto")
#fin mientras
#finCantidad_nombre
