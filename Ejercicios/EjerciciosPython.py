from math import trunc

try:
    salir = False
    opcion = 0
    while (not salir):
        print ("1. Hola Mundo")
        print ("2. A partir de un numero ingresado decir si es mayor o menor o igual a 9")
        print ("3. A partir de un numero ingresado decir si el mismo es par o impar")
        print ("4. Ingresar dos numeros y devuelver el resultado de la suma entre ambos")
        print ("5. Sumar todo los numeros pares entre 2 y 100")
        print ("6. Ingresar un numero y muestre todos los divisores del mismo")
        print ("7. Determinar si un alumno aprueba o suspende un curso") 
        print ("8. Algoritmo: Escriba tu nombre tantas veces como su cantidad ingresada")
        print ("9. Sumar todos los numeros naturales comprendidos entre 1 y 50")
        print ("10. Leer tres numeros; y mostrar la multiplicacion o suma")
        print ("11. Si un numero ingresado es primo o no")
        print ("12. Sumar los digitos de un numero ingresado")

        print ("13. Salir")

        print ("Elige una opcion")
    
        opcion = int(input())
    
        if opcion == 1:
            #1. Hola Mundo
            print("Hola Mundo \n") 

        elif opcion == 2:
            #2. A partir de un numero ingresado diga si es mayor o menor o igual a 9
            num = input("Ingrese un numero ")
            if(num.isdigit()):
                num=int(num)
                if(num > 9):
                    print(f"{num} es mayor a 9 \n")
                elif(num < 9):
                    print(f"{num} es menor a 9 \n")
                else:
                    print(f"{num} es igual a 9 \n")
            else:
                print("Por favor entre un valor numerico")

        elif opcion == 3:
            #3. A partir de un numero ingresado diga si el mismo es par o impar
            num = input("Ingrese un numero ")
            if(num.isdigit()):
                num=int(num)
                if(num % 2 ==0):
                    print(f"{num} es par \n")
                else: 
                    print(f"{num} es impar \n")
            else:
                print("Por favor entre un valor numerico")

        elif opcion == 4:
            #4. Ingresar dos numeros y devuelva el resultado de la suma entre ambos
            num1 = input("Ingrese un numero ")
            num2 = input("Ingrese otro numero ")
            if(num1.isdigit() and num2.isdigit()):
                print(f"La suma de {num1} con {num2} es {int(num1)+int(num2)} \n")
            else:
                print("Los valores entrados no son numeros validos")

        elif opcion == 5:
            #5. Sumar todo los numeros pares entre 2 y 100
            suma = 0
            for numero in range(2,101):
                if(numero % 2 ==0):
                    suma+=numero
            print(f"La suma es {suma} \n")

        elif opcion == 6:
            #6. Ingresar un numero y muestre todos los divisores del mismo
            num = input("Ingrese un numero ")           
            if(num.isdigit()):
                num=int(num)
                for numero in range(1,num+1):
                    if(num %numero==0):
                        print(numero)
            else:
                print("Por favor entre un numero valido")

            print("\n")

        elif opcion == 7:
            #7. Determinar si un alumno aprueba o suspende un curso, sabiendo que aprobara si su
            #   promedio de tres calificaicones es mayor o igual a 4.0; suspende en caso contrario. Debera
            #   permitir ingresar las tres calificaciones y luego calcular su promedio
            calificacion1 = input("Ingrese primer calificacion: ")
            calificacion2 = input("Ingrese segunda calificacion: ")
            calificacion3 = input("Ingrese tercera calificacion: ")
            try:
            #if(calificacion1.isdigit() and calificacion2.isdigit() and calificacion3.isdigit()):                        
                calificacion1=float(calificacion1)
                calificacion2=float(calificacion2)
                calificacion3=float(calificacion3)
                if((calificacion1>=0 and calificacion1<=10)and (calificacion2>=0 and calificacion2<=10) and (calificacion3>=0 and calificacion3<=10)):
                #if((calificacion1 in range(0,11))and (calificacion2 in range(0,11)) and (calificacion3 in range(0,11))):
                    promedio = (calificacion1 +calificacion2+calificacion3)/3
                    if(promedio>=4.0):
                        print (f"Promedio:{promedio},Felicidades! Aprobas el curso :D \n")
                    else: 
                        print (f"Promedio:{promedio},Lamentablemente perdes el curso T.T \n")
                else:
                    print("El rango de las calificaciones no esta entre 0 y 10")
            #else:
            except:
                print("Por favor entre calificaciones con numeros enteros")
            print("\n")

        elif opcion == 8:
            #8. Crear un algoritmo que permita ingresar un nombre y una cantidad numerica para escribir
            #    este nombre tantas veces como su cantidad ingresada
            nombre = input("Ingrese tu nombre: ")
            cantidad = input("Ingrese una cantidad: ")
            if(not nombre.isdigit()):
                if(cantidad.isdigit()):
                    cont=0
                    cantidad=int(cantidad)
                    while(cont<cantidad): 
                        print(nombre)
                        cont+=1
                else:
                    print("Por favor entre una cantidad numerica")
            else:
                print("Por favor entre el nombre en texto")
            print("\n")

        elif opcion == 9:
            #9. Sumar todos los numeros naturales comprendidos entre 1 y 50
            suma = 0
            for numero in range(1,51):
                suma+=numero
            print(f"La suma de los numeros del 1 a 50 es: {suma} \n")
            print("\n")

        elif opcion == 10:
            #10. Leer tres numeros; si el primero es negativo, debe imprimir la multiplicacion
            #   de los tres y si no lo es, imprimira la suma
            num1 = input("Ingrese el primer numero: ")
            num2 = input("Ingrese el segundo numero: ")
            num3 = input("Ingrese el tercer numero: ")
            try:
                num1=int(num1)
                num2=int(num2)
                num3=int(num3)
                if(num1<0):
                    print(f"La multiplicacion de los numeros es:{num1*num2*num3} \n")
                else:
                    print(f"La suma de los numeros es:{num1+num2+num3} \n")
            except ValueError:
                print("Por favor, ingrese un valor numerico")
            except:
                print("Error")
            print("\n")

        elif opcion == 11:   
            #11. Si un numero ingresado es primo o no. (Un numero es primo si es divisible unicamente por 1
            #   y por si mismo)
            num = input("Ingrese un numero: ")
            if(num.isdigit()):
                div=2
                band=True
                num = int(num)
                if(num==1):
                    print("Es primo \n")
                else:
                    #& band==True 
                    while(band==True and num>div ): 
                        if(num % div ==0):
                            band=False
                        div+=1
                    if(band):
                        print(f"{num} es primo \n")
                    else:
                        print(f"{num} no es primo \n")
            else:   
                print("Por Favor, ingresar un valor valido")
        elif opcion == 12:
            #12. Sumar los digitos de un numero ingresado. Ejemplo: Si se ingresa 123, deberia devolver 6
            num = input("Ingrese un numero ")
            if(num.isdigit()):
                num=int(num)
                result=0 
                while(num!=0):
                    result+=num%10
                    num=trunc(num/10)
                print(f"El resultado es: {result} \n")
            else:
                print("Por Favor, ingresar un valor valido")

        elif opcion == 13:
            #13. Salir
            salir = True
        else:
           print ("Introduce un numero entre 1 y 13 \n")
except:
    print ('Ocurrio un Error')
else:
    print("Las instrucciones se completaron en su totalidad")
finally:
    print('Fin del programa')


















