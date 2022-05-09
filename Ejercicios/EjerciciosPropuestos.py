from cmath import pi


try: 
    salir = False
    opcion = 0
    while (not salir):
        print("\n")
        print ("1. Calcular y mostrar el cuadrado de los números del 1 a 30")
        print ("2. Números primos")
        print ("3. Construir un avión de papel")
        print ("4. Realizar las cuatro operaciones básicas")
        print ("5. Volumen y Area de un Cilindro")
        print ("6. Pedir un libro en una biblioteca")
        print ("7. Encontrar el mayor número de tres números")
        print ("8. Factorial de cualquier número")
        print ("9. Encontrar si un numero en mayor o menor a un número dado")
        print ("10. Adivinar una palabra")

        print ("11. Salir")

        print ("Elige una opcion")
        print("\n")

        opcion = int(input())
    
        if opcion == 1:
            #1. Calcular y mostrar el cuadrado de los números del 1 a 30
            for numero in range(1,31):
                print(f"El cuadrado de {numero} es: {numero*numero}")

        elif opcion == 2:
            #2. Números primos
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

        elif opcion == 3:
            #3. Construir un avión de papel
            print("Paso 1: Conseguir Hoja de Papel") 
            print("Paso 2: Doblar el papel a la mitad") 
            print("Paso 3: Doblar la esquina al centro izquierdo") 
            print("Paso 4: Volver a doblar el papel a la mitad") 
            print("Paso 5: Con el papel doblado volver a doblar la esquina al centro izquierdo") 
            print("Paso 6: Doblar hacia abajo para formar alas en ambos lados") 
            print("Paso 7: Comprobar los pasos anteriores") 
            print("Paso 8: (Opcional) Probar que vuela")

        elif opcion == 4:
            #4. Realizar las cuatro operaciones básicas
            num1 = input("Ingrese un numero: ")
            num2 = input("Ingrese otro numero: ")
            try:
                #truquito para usar isdigit con numeros con coma
                #x=123.2
                #x.replace(".","",1).isdigit()
                #obs: split() divide
                num1=float(num1)
                num2=float(num2)
                print(f"La suma es: {num1+num2}")
                print(f"La resta es: {num1-num2}")
                print(f"La multiplicacion es: {num1*num2}")
                while(num2==0):
                    num2 = float(input("No se puede realizar una division por cero, por favor ingrese otro numero:"))
                print(f"La division es: {num1/num2}")
            except:   
                print("Por Favor, ingresar valores numericos validos") 

        elif opcion == 5:
            #5. Volumen y Area de un Cilindro
            radio = input("Ingrese el radio del cilindro: ")
            altura = input("Ingrese la altura del cilindro: ")
            if(radio.isdigit() and altura.isdigit()):
                radio=float(radio)
                altura=float(altura)
                area=2*(pi*pow(radio, 2) ) + 2*pi*radio*altura
                volumen=pi*pow(radio, 2)*altura 
                print(f"El area del cilindro es: {area} y el volumen: {volumen}")
            else:   
                print("Por Favor, ingresar valores validos")   

        elif opcion == 6:
            #6. Pedir un libro en una biblioteca
            print("Paso 1: Ir hasta la Biblioteca") 
            print("Paso 2: Hablar con la Bibliotecaria") 
            print("Paso 3: Informar cual libro quiere llevar") 
            print("Paso 4: Esperar que la bibliotecaria encuentre el libro") 
            print("Paso 5: Mostrar la tarjeta de la Bibliotca a la Bibliotecaria") 
            print("Paso 6: Recoger el libro") 
            print("Paso 7: Volver a casa con el libro") 

        elif opcion == 7:
            #7. Encontrar el mayor número de tres números
            num1 = input("Ingrese el primer numero: ")
            num2 = input("Ingrese el segundo numero: ") 
            num3 = input("Ingrese el tercer numero: ") 
            if(num1.isdigit() and num2.isdigit() and num3.isdigit()):
                if (num1 >= num2 and num1>= num3):
                    print(f"El mayor numero es: {num1}")
                elif (num2>=num1 and num2>=num3):
                    print(f"El mayor numero es: {num2}")
                else:
                    print(f"El mayor numero es: {num3}")
            else:   
                print("Por Favor, ingresar valores validos") 

        elif opcion == 8:
            #8. Factorial de cualquier número
            num = input("Ingrese un numero: ")
            if(num.isdigit()):
                num=int(num)
                fact=1
                for numero in range(1,num+1):
                    fact=fact*numero
                print(f"El factorial de {num} es: {fact}")
            else:   
                print("Por Favor, ingresar un numero valido")  

        elif opcion == 9:
            #9. Encontrar si un numero en mayor o menor a un número dado
            NumeroDado=30
            num = input("Ingrese un numero: ")
            if(num.isdigit()):
                num=int(num)
                if(num>NumeroDado):
                    print(f"Su numero es mayor a {NumeroDado}")
                elif(num<NumeroDado):
                    print(f"Su numero es menor a {NumeroDado}")
                else:
                    print(f"Su numero es igual a {NumeroDado}")
            else:   
                print("Por Favor, ingresar un numero valido") 

        elif opcion == 10:
            #10. Adivinar una palabra
            palabra = "fiesta"
            r = "si"
            # pongo todo en minuscula con: palabra = input().lower()
            while(r != "no"):
                palabraEntrada = input("Entre la palabra a adivinar: ")
                if (palabra == palabraEntrada):
                    print("Has adivinado!!!")
                    break
                else:
                    r = input("No has adivinado. Otra oportunidad (si/no)?")   
        elif opcion == 11:
            #11. Salir
            salir = True        
        else:
            print ("Introduce un numero entre 1 y 11 \n")
except:
    print ('Ocurrio un Error')
else:
    print("Las instrucciones se completaron en su totalidad")
finally:
    print('Fin del programa')    

