from os.path import exists
from random import randint

personas=[]
for n in range(1,101):
    genero=randint(0,1)
    if (genero == 1):
        personas.append("H")
    else:
        personas.append("M")
print(personas)


try:
    file='./Datos_ejercicios01.txt'
    if (exists(file)):
        print('Fichero previamente generado no se sobrescribe')
        fichero=open(file,'rt',encoding='UTF-8')
        contenido=fichero.read()
        print(f'El contenido del fichero es:\n{contenido}')
    else:
        fichero=open(file,"wt",encoding='UTF-8')
        fichero.write(str(personas))
except Exception as e:
    print(f'E:{e}')
finally:
    fichero.close()
    #pass
