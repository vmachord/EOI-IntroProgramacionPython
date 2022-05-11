from random import randint
#personas=[]
#for n in range(1,101):
#   personas.append(randin(0,125))

personas = [randint(0,125) for i in range(1,101)]
print(personas)
mas_de_diezocho = len([persona for persona in personas if persona>=18])
print(mas_de_diezocho)

#Clasificacion
personas.sort()
Clasificacion_Edades= {edad:0 for edad in personas}
for n in personas:
    Clasificacion_Edades[n]+=1
print(Clasificacion_Edades)
edad_mayor=max(personas)
edad_menor=min(personas)

print("Numero de personas con 18 o mas años:",mas_de_diezocho)
print("La edad mas alta es:",edad_mayor)
print("Numero de La edad mas baja es:",edad_menor)

for edad in Clasificacion_Edades:
    print('{:3} -> {:1.2f}%'.format(edad,Clasificacion_Edades[edad]))