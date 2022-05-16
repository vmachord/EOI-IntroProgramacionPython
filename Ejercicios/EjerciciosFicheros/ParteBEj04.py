from os.path import exists

def Proceso(contenido):
    try:
    

        file_resultado='./Ejercicios/EjerciciosFicheros/Resultado_ejercicios04.txt'
        fichero_resultado=open(file_resultado,'wt',encoding='UTF-8')
        dicc=eval(contenido)

        DiccPromedioAnual={} 

        for clave,valor in dicc.items():
            fichero_resultado.write(f'{clave} -> {valor}\n')
            tuplatemperaturas = tuple(valor)
            MediaAnuales = (round(sum(tuplatemperaturas)/12 ,2)) 
            DiccPromedioAnual[clave] = MediaAnuales

        MaxProAnual = max(DiccPromedioAnual.values()) 
        MinProAnual = min(DiccPromedioAnual.values())


        fichero_resultado.write(f'\n La ciudad con el promedio anual mas ALTO es {list(DiccPromedioAnual.keys())[list(DiccPromedioAnual.values()).index(MaxProAnual)]} con un promedio de: {MaxProAnual} ºC \n')
        fichero_resultado.write(f'\n La ciudad con el promedio anual mas BAJO es {list(DiccPromedioAnual.keys())[list(DiccPromedioAnual.values()).index(MinProAnual)]} con un promedio de: {MinProAnual} ºC \n') 

        ListaPromedioAnual = list(DiccPromedioAnual.items()) 
        ListaPromedioAnual.sort(key = lambda x: x[1], reverse=True) 
        fichero_resultado.write(f'La lista de las ciudades ordenadas es :\n{ListaPromedioAnual} \n')

    except Exception as e:
        print(f'E(Proceso):{e}')
    finally:
        fichero_resultado.close()

try:
    file='./Ejercicios/EjerciciosFicheros/Data_ejercicio04.txt'
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