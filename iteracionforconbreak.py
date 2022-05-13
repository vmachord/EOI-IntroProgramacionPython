contadornumero = 0
for numero in range(1,21,2):
    contadornumero+=1
    if(contadornumero>5):
        break #salte a la linea despues del bloque for
    print(numero)
print("Numeros de la serie",contadornumero)