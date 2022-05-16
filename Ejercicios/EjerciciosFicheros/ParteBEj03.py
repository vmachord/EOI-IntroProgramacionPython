from os.path import exists

def Proceso(contenido1,contenido2):
    try:
    
        file_resultado='./Ejercicios/EjerciciosFicheros/Resultado_ejercicios03.txt'
        fichero_resultado=open(file_resultado,'wt',encoding='UTF-8')
        lista_mujeres=eval(contenido1)
        lista_hombres=eval(contenido2)

        lista_mujeres.sort()
        lista_hombres.sort()

        mujeres_mayor_edad = len([i for i in lista_mujeres if i>=18])
        hombres_menor_edad = len([i for i in lista_hombres if i<18])

        fichero_resultado.write(f"Existe una cantidad de {mujeres_mayor_edad} mujeres mayores de edad\n")
        fichero_resultado.write(f"Existe una cantidad de {hombres_menor_edad} hombres menores de edad\n")
        fichero_resultado.write(f"Mujer con menor edad:{lista_mujeres[0]}\n")
        fichero_resultado.write(f"Mujer con mayor edad:{lista_mujeres[len(lista_mujeres)-1]}\n")
        fichero_resultado.write(f"Hombre con menor edad:{lista_hombres[0]}\n")
        fichero_resultado.write(f"Hombre con mayor edad:{lista_hombres[len(lista_hombres)-1]}\n")

        promedio_mujeres=sum(lista_mujeres)/len(lista_mujeres)
        promedio_hombres=sum(lista_hombres)/len(lista_hombres)

        fichero_resultado.write('El promedio de edad de mujeres es: {:1.2f}\n'.format(promedio_mujeres))
        fichero_resultado.write('El promedio de edad de hombres es: {:1.2f}\n'.format(promedio_hombres))

    except Exception as e:
        print(f'E(Proceso):{e}')
    finally:
        fichero_resultado.close()

try:
    file1='./Ejercicios/EjerciciosFicheros/Data_chicas_ejercicio03.txt'
    file2='./Ejercicios/EjerciciosFicheros/Data_chicos_ejercicio03.txt'
    if(exists(file1) and exists(file2)):
        fichero1=open(file1,'rt',encoding='UTF-8')
        fichero2=open(file2,'rt',encoding='UTF-8')
        contenido1=fichero1.read()
        contenido2=fichero2.read()
        Proceso(contenido1,contenido2)
        print(f'Procesado ficheros:{file1}{file2}')
    else:
        print('No podemos procesar la informacion')
except Exception as e:
    print(f'E:{e}')
finally:
    fichero1.close()
    fichero2.close()