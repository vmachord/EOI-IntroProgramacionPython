from random import randint

mi_lista = []

for i in range(1,101):
        mi_lista.append(randint(1,120))
mi_lista.sort()    
mayor_de_18=0 
porcentaje_edades = dict()                   

for edades in mi_lista:
    if(edades>=18):
        mayor_de_18+=1
    if(edades in porcentaje_edades):
        porcentaje_edades[edades]+=1
    else:
        porcentaje_edades[edades]=1

print("Porcentaje de edades:")
for k in porcentaje_edades.keys():
    print(f"Con {k} años: {porcentaje_edades[k]*100/len(mi_lista)}%")

print(f"La persona con menor edad tiene: {mi_lista[0]} año(s)")
print(f"La persona con mayor edad tiene: {mi_lista[len(mi_lista)-1]} año(s)")
print(f"\nHay un total de {mayor_de_18} personas mayores de 18:")