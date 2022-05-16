from random import randint
from os.path import exists

def lee_o_crea_fichero_apartir_de_una_lista(file,personas):
    try:
        if(exists(file)):
            fichero = open(file,'rt',encoding='UTF-8')
            contenido = fichero.read()
            print(f'Fichero previamente creado, este es su contenido:\n{contenido}')
        else:
            fichero = open(file,'wt',encoding='UTF-8')
            fichero.write(str(personas))
            print(f'Fichero:{file} - generado')
    except Exception as e:
        print(f'E:{e}')
    finally:
        fichero.close()

print(f'Ejecucion 02:{__name__}')
if __name__ == '__main__':
    personas=[]
    for n in range(1,101):
        personas.append(randint(0,125))

    personas1 = [randint(0,125) for i in range(1,101)]

    file = './Ejercicios/EjerciciosFicheros/Datos_ejercicio02.txt'
    file1 = './Ejercicios/EjerciciosFicheros/Datos_ejercicio02A.txt'

    lee_o_crea_fichero_apartir_de_una_lista(file,personas)
    lee_o_crea_fichero_apartir_de_una_lista(file1,personas1)