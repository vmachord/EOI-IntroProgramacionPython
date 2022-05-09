from random import randint

mi_lista = []

for i in range(1,101):
    mi_lista.append(randint(0,1))

cant_hombres = 0
cant_mujeres = 0

for j in mi_lista:
    if(j==0):
        cant_mujeres+=1
    else:
        cant_hombres+=1

print(f"El porcentaje de mujeres es: {cant_mujeres*100/len(mi_lista)}%")
print(f"El porcentaje de hombres es: {cant_hombres*100/len(mi_lista)}%")


if (cant_mujeres>cant_hombres):
    print("Hay mas mujeres que hombres")
elif (cant_mujeres<cant_hombres):
    print("Hay mas hombres que mujeres")
else:
    print("Hay una cantidad igual de hombres y mujeres")