#Suma de Pares
suma = 0
nro = 2
#se puede incrementar de a dos
while (nro<=100):
    if(nro%2 == 0):
        suma=suma+nro
    #fin si
    nro=nro+1
#fin while
print(f"la suma de los pares entre 2 y 100 es {suma}")