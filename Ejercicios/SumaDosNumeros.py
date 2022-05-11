Num1=input("Escribir el numero 1:")
Num2=input("Escribir el numero 2:")
if(Num1.isdigit() and Num2.isdigit()):
    print(f"El resultado es: {int(Num1) + int(Num2)}")
else:
    print("Los valores entrados no son numeros validos")