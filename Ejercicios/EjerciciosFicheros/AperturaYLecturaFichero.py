from os.path import exists
#def fichero_existe(file):
#    try:
#        open(file)
#    except FileNotFoundError:
#        return False
#    return True

try:
    #fichero = open('file_500.txt','rt',encoding='UTF-8')
    #print(type(fichero))
    #contenido=fichero.read()
    #print(contenido)

    #file='file_300.txt'
    #fichero=open(file,"wt",encoding='UTF-8')
    #contenido2="'arbol','limon','naranja'"
    #fichero.write(contenido2)
    #print('fin de la cita ..')

    file='./file_510.csv'
    #fichero_existe=True
    if(exists(file)):
        fichero=open(file,'rt',encoding='UTF-8')
        contenido=fichero.read()
        if (len(contenido)>0):
            print(contenido)
        else:
            print('El fichero no tiene contenido')
    else:
        fichero=open(file,'wt',encoding='UTF-8')
        contenido = f'{file}fichero510,arbol,limon,mandarina,naranja'
        fichero.write(contenido)
        print('escriot el contenido')
except Exception as e:
    print(f'E:{e}')
finally:
    fichero.close()