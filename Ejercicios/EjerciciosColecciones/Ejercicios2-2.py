from random import randint
import operator

personas = dict()

for i in range(1,101):
        nombre=input("Nombre:")
        while(nombre in personas or nombre==''):
                nombre=input("Nombre ivalido.Digite otro nombre:")
        personas[nombre]=randint(1,120)


#key- Una funcion que sirve como llave para la comparacion de classificacion
personas_sort = sorted(personas.items(), key=operator.itemgetter(1))

mayor_de_18=0 
porcentaje_edades = dict()                   

print(personas_sort)

for edades in personas.keys():
    if(personas[edades]>=18):
        mayor_de_18+=1
    if(personas[edades] in porcentaje_edades):
        porcentaje_edades[personas[edades]]+=1
    else:
        porcentaje_edades[personas[edades]]=1

print("Porcentaje de edades:")
for k in porcentaje_edades.keys():
    print(f"Con {k} años: {porcentaje_edades[k]*100//len(personas_sort)}%")

menor_edad=personas_sort[0][0]
mayor_edad=personas_sort[len(personas_sort)-1][0]

print("La(s) persona(s) con menor edad es(son):")
for i in range (1,len(personas)):
    print(f"{menor_edad} con {personas[menor_edad]} año(s)")
    if(personas_sort[i][1]==personas[menor_edad]):
        menor_edad=personas_sort[i][0]
    else:
        break

print("\nLa(s) persona(s) con mayor edad es(son):")
for i in range (len(personas)-2,0,-1):
    print(f"{mayor_edad} con {personas[mayor_edad]} año(s)")
    if(personas_sort[i][1]==personas[mayor_edad]):
        mayor_edad=personas_sort[i][0]
    else:
        break

print(f"\nHay un total de {mayor_de_18} personas mayores de 18:")









#------------------------------------------------------------------------------------------------
#print(f"{personas_sort[0][0]} tiene la menor edad con: {personas[personas_sort[0][0]]} año(s)")
#print(f"{personas_sort[len(personas_sort)-1][0]} tiene la mayor edad con: {personas[personas_sort[len(personas_sort)-1][0]]} año(s)")

#datos de prueba:
#personas['Sofia']=12
#personas['Camila']=12
#personas['Teresa']=30
#personas['Andresa']=34
#personas['Vanessa']=120
#personas['Renata']=120