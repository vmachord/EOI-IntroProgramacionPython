from os.path import exists

def Proceso(contenido):
    try:
        #convierto cadenas de carcteres a listas
        lista=eval(contenido)
        #personas=['H', 'H', 'M', 'H', 'H', 'M', 'M', 'H', 'M', 'M', 'M', 'M', 'M', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'M', 'M', 'H', 'H', 'M', 'M', 'M', 'H', 'M', 'M', 'H', 'H', 'H', 'M', 'M', 'M', 'H', 'H', 'H', 'M', 'H', 'H', 'H', 'M', 'H', 'H', 'H', 'H', 'M', 'M', 'H', 'M', 'H', 'H', 'M', 'M', 'M', 'M', 'H', 'M', 'H', 'H', 'M', 'M', 'M', 'H', 'H', 'M', 'H', 'M', 'H', 'M', 'H', 'H', 'H', 'M', 'H', 'M', 'M', 'M', 'M', 'H', 'H', 'M', 'H', 'H', 'H', 'H', 'H', 'M', 'H', 'H', 'M', 'H', 'M', 'H', 'M', 'M', 'H']
        
        file_resultado='./Ejercicios/EjerciciosFicheros/Resultado_ejercicios01.txt'
        fichero_resultado=open(file_resultado,'wt',encoding='UTF-8')
        lista=eval(contenido)
        fichero_resultado.write(f"El porcentaje de mujeres es del: {lista.count('M')}%\n")
        fichero_resultado.write(f"El porcentaje de hombres es del: {lista.count('H')}%\n")   
        if(lista.count('M')>lista.count('H')):
            fichero_resultado.write("Hay mas mujeres que hombres\n")
        elif(lista.count('H')==lista.count('M')):
            fichero_resultado.write("Hay igualdad")
        else: 
            fichero_resultado.write("Hay mas hombres que mujeres\n")
    except Exception as e:
        print(f'E(Proceso):{e}')
    finally:
        fichero_resultado.close()

try:
    file='./Ejercicios/EjerciciosFicheros/Datos_ejercicios01.txt'
    if(exists(file)):
        fichero=open(file,'rt',encoding='UTF-8')
        contenido=fichero.read()
        Proceso(contenido)
        print(f'Procesado fichero:{file}')
    else:
        print('No podemos procesar la informacion')
except Exception as e:
    print(f'E:{e}')
finally:
    fichero.close()