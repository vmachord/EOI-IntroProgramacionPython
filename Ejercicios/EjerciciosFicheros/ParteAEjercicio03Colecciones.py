from random import randint
from Ejercicio2Colecciones import lee_o_crea_fichero_apartir_de_una_lista as lee_escribir

print(f'Ejecucion 03:{__name__}')

mujeres=[]
hombres=[]

genero=[randint(0,1) for n in range(1,101)]
mujeres=[randint(0,101) for g in genero if g==1]
hombres=[randint(0,101) for g in genero if g==0]

fileChicos='./Ejercicios/EjerciciosFicheros/Data_chicos_ejercicio03.txt'
fileChicas='./Ejercicios/EjerciciosFicheros/Data_chicas_ejercicio03.txt'

lee_escribir(fileChicas,mujeres)
lee_escribir(fileChicos,hombres)