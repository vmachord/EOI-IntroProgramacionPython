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
            num = int(input("Ingrese un numero "))
            if(num > 9):
                print(f"{num} es mayor a 9 \n")
            elif(num < 9):
                print(f"{num} es menor a 9 \n")
            else:
                print(f"{num} es igual a 9 \n")

        elif opcion == 3:
            #3. A partir de un numero ingresado diga si el mismo es par o impar
            num = int(input("Ingrese un numero "))
            if(num % 2 ==0):
                print(f"{num} es par \n")
            else: 
                print(f"{num} es impar \n")

        elif opcion == 4:
            #4. Ingresar dos numeros y devuelva el resultado de la suma entre ambos
            num1 = int(input("Ingrese un numero "))
            num2 = int(input("Ingrese otro numero "))
            print(f"La suma de {num1} con {num2} es {num1+num2} \n")

        elif opcion == 5:
            #5. Sumar todo los numeros pares entre 2 y 100
            suma = 0
            for numero in range(2,101):
                if(numero % 2 ==0):
                    suma+=numero
            print(f"La suma es {suma} \n")

        elif opcion == 6:
            #6. Ingresar un numero y muestre todos los divisores del mismo
            num = int(input("Ingrese un numero "))
            for numero in range(1,num+1):
                if(num %numero==0):
                    print(numero)
            print("\n")

        elif opcion == 7:
            #7. Determinar si un alumno aprueba o suspende un curso, sabiendo que aprobara si su
            #   promedio de tres calificaicones es mayor o igual a 4.0; suspende en caso contrario. Debera
            #   permitir ingresar las tres calificaciones y luego calcular su promedio
            calificacion1 = float(input("Ingrese primer calificacion "))
            calificacion2 = float(input("Ingrese segunda calificacion "))
            calificacion3 = float(input("Ingrese tercera calificacion "))

            promedio = (calificacion1 +calificacion2+ calificacion3)/3
            if(promedio>=4.0):
                print (f"Promedio:{promedio},Felicidades! Aprobas el curso :D \n")
            else: 
                print (f"Promedio:{promedio},Lamentablemente perdes el curso T.T \n")

        elif opcion == 8:
            #8. Crear un algoritmo que permita ingresar un nombre y una cantidad numerica para escribir
            #    este nombre tantas veces como su cantidad ingresada
            nombre = input("Ingrese tu nombre ")
            cantidad = int(input("Ingrese una cantidad "))
            cont=0
            while(cont<cantidad): 
                print(nombre)
                cont+=1
            print("\n")

        elif opcion == 9:
            #9. Sumar todos los numeros naturales comprendidos entre 1 y 50
            suma = 0
            for numero in range(1,51):
                suma+=numero
            print(f"La suma de los numeros del 1 a 50 es: {suma} \n")
        elif opcion == 10:
            #10. Leer tres numeros; si el primero es negativo, debe imprimir la multiplicacion
            #   de los tres y si no lo es, imprimira la suma
            num1 = int(input("Ingrese primer numero "))
            num2 = int(input("Ingrese segundo numero "))
            num3 = int(input("Ingrese tercer numero "))
            if(num1<0):
                print(f"La multiplicacion de los numeros es:{num1*num2*num3} \n")
            else:
                print(f"La suma de los numeros es:{num1+num2+num3} \n")

        elif opcion == 11:   
            #11. Si un numero ingresado es primo o no. (Un numero es primo si es divisible unicamente por 1
            #   y por si mismo)
            num = int(input("Ingrese un numero "))
            div=2
            band=True
            if(num==1):
                print("Es primo \n")
            else:
                #& band==True 
                while(band==True and num>div ): 
                    if(num % div ==0):
                        band=False
                    div+=1
                if(band):
                    print("Es primo \n")
                else:
                    print("No es primo \n")

        elif opcion == 12:
            #12. Sumar los digitos de un numero ingresado. Ejemplo: Si se ingresa 123, deberia devolver 6
            num = int(input("Ingrese un numero "))
            result=0
            while(num!=0):
                result+=num%10
                num=trunc(num/10)
            print(f"El resultado es: {result} \n")

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


















