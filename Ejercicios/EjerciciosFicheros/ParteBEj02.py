from os.path import exists

def Proceso(contenido):
    try:
    
        file_resultado='./Ejercicios/EjerciciosFicheros/Resultado_ejercicios02.txt'
        fichero_resultado=open(file_resultado,'wt',encoding='UTF-8')
        personas=eval(contenido)
        fichero_resultado.write(f"Numero de personas con 18 o mas años: {len([persona for persona in personas if persona>=18])}%\n")  
        personas.sort()
        fichero_resultado.write(f"La edad mas alta es:{max(personas)}\n")
        fichero_resultado.write(f"La edad mas baja es:{min(personas)}\n")
        porcentaje_edades = dict()                   
        for edades in personas:
            if(edades in porcentaje_edades):
                porcentaje_edades[edades]+=1
            else:
                porcentaje_edades[edades]=1

        fichero_resultado.write("Porcentaje de edades:\n")
        for k in porcentaje_edades.keys():
            fichero_resultado.write(f"Con {k} años: {porcentaje_edades[k]*100/len(personas)}%\n")

    except Exception as e:
        print(f'E(Proceso):{e}')
    finally:
        fichero_resultado.close()

try:
    file='./Ejercicios/EjerciciosFicheros/Datos_ejercicio02.txt'
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