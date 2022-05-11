#Algoritmo SumaDigitos
nro = input("Ingrese un numero ")
if(nro.isdigit()):
    nro = int(nro)
    result=0 
    while(nro!=0):
        result+=nro%10
        nro=nro//10
    print(f"El resultado es: {result}")
else:
    print("Entre un numero basico")