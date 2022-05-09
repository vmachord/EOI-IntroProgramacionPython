from random import randint

lista_mujeres = []
lista_hombres = []

#llenar listas
for i in range(1,101):
    if(randint(0,1)==0):
        lista_mujeres.append(randint(1,120))
    else:
        lista_hombres.append(randint(1,120))

print(lista_mujeres)
print(lista_hombres)

promedio_hombres=0
promedio_mujeres=0
mujeres_mayor_edad=0

for i in lista_mujeres:
    promedio_mujeres+=i
    if(i>=18):
        mujeres_mayor_edad+=1

for i in lista_hombres:
    promedio_hombres+=i

print(f"Existe una cantidad de {mujeres_mayor_edad} mujeres mayores de edad")
print(f"El promedio de edad de mujeres es: {promedio_mujeres//len(lista_mujeres)}")
print(f"El promedio de edad de hombres es: {promedio_hombres//len(lista_hombres)}")

