from random import randint
lista_mujeres = []
lista_hombres = []

for i in range(1,101):
    randomm=randint(0,1)
    if(randomm==0):
        lista_mujeres.append(randomm)
    else:
        lista_hombres.append(randomm)

print(f"El porcentaje de mujeres es: {len(lista_mujeres)*100/(len(lista_mujeres)+len(lista_hombres))}%")
print(f"El porcentaje de hombres es: {len(lista_hombres)*100/(len(lista_hombres)+len(lista_mujeres))}%")

if (len(lista_mujeres)>len(lista_hombres)):
    print("Hay mas mujeres que hombres")
elif (len(lista_mujeres)<len(lista_hombres)):
    print("Hay mas hombres que mujeres")
else:
    print("Hay una cantidad igual de hombres y mujeres")