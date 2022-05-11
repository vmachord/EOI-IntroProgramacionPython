from random import randint

lista_mujeres = []
lista_hombres = []

#llenar listas
#for i in range(1,101):
#    if(randint(0,1)==0):
#        lista_mujeres.append(randint(1,120))
#    else:
#        lista_hombres.append(randint(1,120))

#reemplazo lo anterior
genero = [randint(0,1) for n in range(1,101)]
lista_mujeres = [randint(1,120) for g in genero if g==1]
lista_hombres = [randint(1,120) for g in genero if g==0]

lista_mujeres.sort()
lista_hombres.sort()

print(lista_mujeres)
print(lista_hombres)

mujeres_mayor_edad = len([i for i in lista_mujeres if i>=18])
hombres_menor_edad = len([i for i in lista_hombres if i<18])

#for i in lista_mujeres:
#    promedio_mujeres+=i

promedio_mujeres=sum(lista_mujeres)/len(lista_mujeres)

#for i in lista_hombres:
#    promedio_hombres+=i

promedio_hombres=sum(lista_hombres)/len(lista_hombres)

print(f"Existe una cantidad de {mujeres_mayor_edad} mujeres mayores de edad")
print(f"Existe una cantidad de {hombres_menor_edad} hombres menores de edad")
print(f"Mujer con menor edad:{lista_mujeres[0]}")
print(f"Mujer con mayor edad:{lista_mujeres[len(lista_mujeres)-1]}")
print(f"Hombre con menor edad:{lista_hombres[0]}")
print(f"Hombre con mayor edad:{lista_hombres[len(lista_hombres)-1]}")
print(f"El promedio de edad de mujeres es: {promedio_mujeres}")
print(f"El promedio de edad de hombres es: {promedio_hombres}")

